from admin_module import Admin

local_admin = Admin('Steven', 'Sanie', 23, 'male', 'lusaka')

local_admin.describe_user()
local_admin.show_privileges(local_admin.f_name)