from fastapi import HTTPException

class PermissionChecker:
    def check_owner(board, current_user):
        if board.owner_id != current_user.id:
            raise HTTPException(status_code=403, detail="Only the owner of this board can perform this action.")