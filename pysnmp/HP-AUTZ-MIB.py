#
# PySNMP MIB module HP-AUTZ-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-AUTZ-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:20:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
VlanIndex, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Gauge32, Bits, Counter32, ObjectIdentity, TimeTicks, Counter64, Unsigned32, MibIdentifier, ModuleIdentity, IpAddress, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Gauge32", "Bits", "Counter32", "ObjectIdentity", "TimeTicks", "Counter64", "Unsigned32", "MibIdentifier", "ModuleIdentity", "IpAddress", "Integer32")
RowStatus, TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TruthValue", "DisplayString", "TextualConvention")
hpSwitchAuthorizationMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32))
hpSwitchAuthorizationMIB.setRevisions(('2017-03-16 00:00', '2016-10-20 00:00', '2016-05-09 00:00', '2016-01-07 00:00', '2014-08-04 00:00', '2011-02-07 00:00', '2007-08-29 00:00', '2005-10-05 00:00',))
if mibBuilder.loadTexts: hpSwitchAuthorizationMIB.setLastUpdated('201703160000Z')
if mibBuilder.loadTexts: hpSwitchAuthorizationMIB.setOrganization('HP Networking')
class HpAutzUserRoleName(TextualConvention, OctetString):
    status = 'current'
    displayHint = '63a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 63)

hpicfSwitchAuthorizationNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 0))
hpicfSwitchAuthServerFail = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 0, 1)).setObjects(("HP-AUTZ-MIB", "hpicfSwitchAuthServerType"), ("HP-AUTZ-MIB", "hpicfSwitchAuthServerIPType"), ("HP-AUTZ-MIB", "hpicfSwitchAuthServerIP"))
if mibBuilder.loadTexts: hpicfSwitchAuthServerFail.setStatus('current')
hpSwitchAuthorizationConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1))
hpSwitchAutzServiceTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 1), )
if mibBuilder.loadTexts: hpSwitchAutzServiceTable.setStatus('current')
hpSwitchAutzServiceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 1, 1), ).setIndexNames((0, "HP-AUTZ-MIB", "hpSwitchAutzServiceType"))
if mibBuilder.loadTexts: hpSwitchAutzServiceEntry.setStatus('current')
hpSwitchAutzServiceType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("commands", 1), ("exec", 2), ("network", 3))))
if mibBuilder.loadTexts: hpSwitchAutzServiceType.setStatus('current')
hpSwitchAutzServicePrimaryMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("local", 1), ("tacacs", 2), ("radius", 3), ("none", 4), ("auto", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpSwitchAutzServicePrimaryMethod.setStatus('current')
hpSwitchAutzServiceSecondaryMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("local", 1), ("none", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpSwitchAutzServiceSecondaryMethod.setStatus('current')
hpSwitchAutzServiceCommandsLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("all", 1), ("managerlevelonly", 2))).clone('all')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpSwitchAutzServiceCommandsLevel.setStatus('current')
hpicfSwitchAuthObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 2))
hpicfSwitchAuthServerType = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 9))).clone(namedValues=NamedValues(("radius", 1), ("tacacs", 2), ("other", 9)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpicfSwitchAuthServerType.setStatus('current')
hpicfSwitchAuthServerIPType = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 2, 2), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpicfSwitchAuthServerIPType.setStatus('current')
hpicfSwitchAuthServerIP = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 2, 3), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpicfSwitchAuthServerIP.setStatus('current')
hpSwitchAuthConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 3))
hpicfSwitchAuthServerNotifyEnable = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfSwitchAuthServerNotifyEnable.setStatus('current')
hpSwitchAuthLocalPrivConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 4))
hpSwitchLocalMgmtPrivGroupsTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 4, 1), )
if mibBuilder.loadTexts: hpSwitchLocalMgmtPrivGroupsTable.setStatus('current')
hpSwitchLocalMgmtPrivGroupsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 4, 1, 1), ).setIndexNames((0, "HP-AUTZ-MIB", "hpSwitchLocalMgmtPrivGroupIndex"))
if mibBuilder.loadTexts: hpSwitchLocalMgmtPrivGroupsEntry.setStatus('current')
hpSwitchLocalMgmtPrivGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: hpSwitchLocalMgmtPrivGroupIndex.setStatus('current')
hpSwitchLocalMgmtPrivGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 4, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchLocalMgmtPrivGroupName.setStatus('current')
hpSwitchLocalMgmtPrivGroupStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 4, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchLocalMgmtPrivGroupStatus.setStatus('current')
hpSwitchLocalMgmtPrivCommandsTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 4, 2), )
if mibBuilder.loadTexts: hpSwitchLocalMgmtPrivCommandsTable.setStatus('current')
hpSwitchLocalMgmtPrivCommandsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 4, 2, 1), ).setIndexNames((0, "HP-AUTZ-MIB", "hpSwitchLocalMgmtPrivGroupIndex"), (0, "HP-AUTZ-MIB", "hpSwitchLocalMgmtPrivCmdSequenceIndex"))
if mibBuilder.loadTexts: hpSwitchLocalMgmtPrivCommandsEntry.setStatus('current')
hpSwitchLocalMgmtPrivCmdSequenceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: hpSwitchLocalMgmtPrivCmdSequenceIndex.setStatus('current')
hpSwitchLocalMgmtPrivCmdMatchStr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 4, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchLocalMgmtPrivCmdMatchStr.setStatus('current')
hpSwitchLocalMgmtPrivCmdPriv = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 4, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("permit", 1), ("deny", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchLocalMgmtPrivCmdPriv.setStatus('current')
hpSwitchLocalMgmtPrivCmdSendLog = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 4, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchLocalMgmtPrivCmdSendLog.setStatus('current')
hpSwitchLocalMgmtPrivCmdStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 4, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchLocalMgmtPrivCmdStatus.setStatus('current')
hpSwitchAutzUserRole = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5))
hpSwitchAutzUserRoleEnabled = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpSwitchAutzUserRoleEnabled.setStatus('current')
hpSwitchAutzUserRoleInitialRoleName = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 2), HpAutzUserRoleName()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpSwitchAutzUserRoleInitialRoleName.setStatus('current')
hpSwitchAutzUserRoleDownloadedEnabled = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 4), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpSwitchAutzUserRoleDownloadedEnabled.setStatus('current')
hpSwitchAutzUserRoleTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 3), )
if mibBuilder.loadTexts: hpSwitchAutzUserRoleTable.setStatus('current')
hpSwitchAutzUserRoleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 3, 1), ).setIndexNames((0, "HP-AUTZ-MIB", "hpSwitchAutzUserRoleName"))
if mibBuilder.loadTexts: hpSwitchAutzUserRoleEntry.setStatus('current')
hpSwitchAutzUserRoleName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 3, 1, 1), HpAutzUserRoleName())
if mibBuilder.loadTexts: hpSwitchAutzUserRoleName.setStatus('current')
hpSwitchAutzUserRoleRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 3, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchAutzUserRoleRowStatus.setStatus('current')
hpSwitchAutzUserRoleType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("predefined", 1), ("local", 2), ("downloaded", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpSwitchAutzUserRoleType.setStatus('current')
hpSwitchAutzUserRoleCaptivePortalProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 3, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchAutzUserRoleCaptivePortalProfileName.setStatus('current')
hpSwitchAutzUserRoleIngressUserPolicyName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 3, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchAutzUserRoleIngressUserPolicyName.setStatus('current')
hpSwitchAutzUserRoleReauthPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 999999999))).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchAutzUserRoleReauthPeriod.setStatus('current')
hpSwitchAutzUserRoleVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 3, 1, 7), VlanIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchAutzUserRoleVlanId.setStatus('current')
hpSwitchAutzUserRoleVlanName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 3, 1, 8), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchAutzUserRoleVlanName.setStatus('current')
hpSwitchAutzUserRoleTunneledNodeServerRedirect = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 3, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchAutzUserRoleTunneledNodeServerRedirect.setStatus('current')
hpSwitchAutzUserRoleTunneledNodeServerSecondaryRole = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 3, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchAutzUserRoleTunneledNodeServerSecondaryRole.setStatus('current')
hpSwitchAutzUserRoleTaggedVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 3, 1, 11), VlanIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchAutzUserRoleTaggedVlanId.setStatus('current')
hpSwitchAutzUserRoleTaggedVlanName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 3, 1, 12), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchAutzUserRoleTaggedVlanName.setStatus('current')
hpSwitchAuthorizationConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2))
hpSwitchAuthorizationMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 1))
hpSwitchAuthorizationMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 1, 1)).setObjects(("HP-AUTZ-MIB", "hpSwitchAuthorizationConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchAuthorizationMIBCompliance = hpSwitchAuthorizationMIBCompliance.setStatus('current')
hpSwitchLocalMgmtPrivGrpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 1, 2)).setObjects(("HP-AUTZ-MIB", "hpSwitchAutzLocalMgmtPrivGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchLocalMgmtPrivGrpMIBCompliance = hpSwitchLocalMgmtPrivGrpMIBCompliance.setStatus('current')
hpSwitchLocalMgmtPrivGrpMIBCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 1, 3)).setObjects(("HP-AUTZ-MIB", "hpSwitchAutzLocalMgmtPrivGroup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchLocalMgmtPrivGrpMIBCompliance1 = hpSwitchLocalMgmtPrivGrpMIBCompliance1.setStatus('current')
hpSwitchAuthorizationObjectsGrpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 1, 4)).setObjects(("HP-AUTZ-MIB", "hpicfSwitchAuthorizationObjectsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchAuthorizationObjectsGrpMIBCompliance = hpSwitchAuthorizationObjectsGrpMIBCompliance.setStatus('current')
hpSwitchAuthorizationNotificationGrpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 1, 5)).setObjects(("HP-AUTZ-MIB", "hpicfSwitchAuthorizationNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchAuthorizationNotificationGrpMIBCompliance = hpSwitchAuthorizationNotificationGrpMIBCompliance.setStatus('current')
hpSwitchAutzRoleGrpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 1, 6)).setObjects(("HP-AUTZ-MIB", "hpSwitchAutzUserRoleGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchAutzRoleGrpCompliance = hpSwitchAutzRoleGrpCompliance.setStatus('deprecated')
hpSwitchAutzRoleGrpCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 1, 7)).setObjects(("HP-AUTZ-MIB", "hpSwitchAutzUserRoleGroup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchAutzRoleGrpCompliance1 = hpSwitchAutzRoleGrpCompliance1.setStatus('deprecated')
hpSwitchAutzRoleGrpCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 1, 8)).setObjects(("HP-AUTZ-MIB", "hpSwitchAutzUserRoleGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchAutzRoleGrpCompliance2 = hpSwitchAutzRoleGrpCompliance2.setStatus('deprecated')
hpSwitchAutzRoleGrpCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 1, 9)).setObjects(("HP-AUTZ-MIB", "hpSwitchAutzUserRoleGroup3"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchAutzRoleGrpCompliance3 = hpSwitchAutzRoleGrpCompliance3.setStatus('current')
hpSwitchAuthorizationMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 2))
hpSwitchAuthorizationConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 2, 1)).setObjects(("HP-AUTZ-MIB", "hpSwitchAutzServicePrimaryMethod"), ("HP-AUTZ-MIB", "hpSwitchAutzServiceSecondaryMethod"), ("HP-AUTZ-MIB", "hpSwitchAutzServiceCommandsLevel"), ("HP-AUTZ-MIB", "hpicfSwitchAuthServerNotifyEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchAuthorizationConfigGroup = hpSwitchAuthorizationConfigGroup.setStatus('current')
hpicfSwitchAuthorizationNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 2, 2)).setObjects(("HP-AUTZ-MIB", "hpicfSwitchAuthServerFail"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSwitchAuthorizationNotificationGroup = hpicfSwitchAuthorizationNotificationGroup.setStatus('current')
hpicfSwitchAuthorizationObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 2, 3)).setObjects(("HP-AUTZ-MIB", "hpicfSwitchAuthServerType"), ("HP-AUTZ-MIB", "hpicfSwitchAuthServerIPType"), ("HP-AUTZ-MIB", "hpicfSwitchAuthServerIP"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSwitchAuthorizationObjectsGroup = hpicfSwitchAuthorizationObjectsGroup.setStatus('current')
hpSwitchAutzLocalMgmtPrivGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 2, 4)).setObjects(("HP-AUTZ-MIB", "hpSwitchLocalMgmtPrivGroupName"), ("HP-AUTZ-MIB", "hpSwitchLocalMgmtPrivCmdMatchStr"), ("HP-AUTZ-MIB", "hpSwitchLocalMgmtPrivCmdPriv"), ("HP-AUTZ-MIB", "hpSwitchLocalMgmtPrivCmdSendLog"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchAutzLocalMgmtPrivGroup = hpSwitchAutzLocalMgmtPrivGroup.setStatus('current')
hpSwitchAutzLocalMgmtPrivGroup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 2, 5)).setObjects(("HP-AUTZ-MIB", "hpSwitchLocalMgmtPrivCmdStatus"), ("HP-AUTZ-MIB", "hpSwitchLocalMgmtPrivGroupStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchAutzLocalMgmtPrivGroup1 = hpSwitchAutzLocalMgmtPrivGroup1.setStatus('current')
hpSwitchAutzUserRoleGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 2, 6)).setObjects(("HP-AUTZ-MIB", "hpSwitchAutzUserRoleEnabled"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleInitialRoleName"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleRowStatus"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleType"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleCaptivePortalProfileName"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleIngressUserPolicyName"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleReauthPeriod"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleVlanId"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleVlanName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchAutzUserRoleGroup = hpSwitchAutzUserRoleGroup.setStatus('deprecated')
hpSwitchAutzUserRoleGroup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 2, 7)).setObjects(("HP-AUTZ-MIB", "hpSwitchAutzUserRoleEnabled"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleInitialRoleName"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleRowStatus"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleType"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleCaptivePortalProfileName"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleIngressUserPolicyName"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleReauthPeriod"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleVlanId"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleVlanName"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleTunneledNodeServerRedirect"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleTunneledNodeServerSecondaryRole"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchAutzUserRoleGroup1 = hpSwitchAutzUserRoleGroup1.setStatus('deprecated')
hpSwitchAutzUserRoleGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 2, 8)).setObjects(("HP-AUTZ-MIB", "hpSwitchAutzUserRoleEnabled"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleInitialRoleName"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleRowStatus"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleType"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleCaptivePortalProfileName"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleIngressUserPolicyName"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleReauthPeriod"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleVlanId"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleVlanName"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleTunneledNodeServerRedirect"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleTunneledNodeServerSecondaryRole"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleTaggedVlanId"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleTaggedVlanName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchAutzUserRoleGroup2 = hpSwitchAutzUserRoleGroup2.setStatus('deprecated')
hpSwitchAutzUserRoleGroup3 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 2, 9)).setObjects(("HP-AUTZ-MIB", "hpSwitchAutzUserRoleEnabled"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleInitialRoleName"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleRowStatus"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleType"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleCaptivePortalProfileName"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleIngressUserPolicyName"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleReauthPeriod"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleVlanId"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleVlanName"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleTunneledNodeServerRedirect"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleTunneledNodeServerSecondaryRole"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleTaggedVlanId"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleTaggedVlanName"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleDownloadedEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchAutzUserRoleGroup3 = hpSwitchAutzUserRoleGroup3.setStatus('current')
mibBuilder.exportSymbols("HP-AUTZ-MIB", hpSwitchAutzUserRoleInitialRoleName=hpSwitchAutzUserRoleInitialRoleName, hpicfSwitchAuthServerIPType=hpicfSwitchAuthServerIPType, hpicfSwitchAuthorizationNotifications=hpicfSwitchAuthorizationNotifications, hpSwitchAuthorizationObjectsGrpMIBCompliance=hpSwitchAuthorizationObjectsGrpMIBCompliance, hpSwitchAutzRoleGrpCompliance1=hpSwitchAutzRoleGrpCompliance1, hpSwitchAutzUserRoleGroup3=hpSwitchAutzUserRoleGroup3, hpicfSwitchAuthServerIP=hpicfSwitchAuthServerIP, hpicfSwitchAuthObjects=hpicfSwitchAuthObjects, hpSwitchAutzUserRoleTable=hpSwitchAutzUserRoleTable, hpSwitchAutzUserRoleTunneledNodeServerSecondaryRole=hpSwitchAutzUserRoleTunneledNodeServerSecondaryRole, hpSwitchAuthorizationConformance=hpSwitchAuthorizationConformance, hpSwitchLocalMgmtPrivGroupsEntry=hpSwitchLocalMgmtPrivGroupsEntry, hpSwitchAutzUserRoleVlanId=hpSwitchAutzUserRoleVlanId, hpSwitchAutzUserRoleTaggedVlanId=hpSwitchAutzUserRoleTaggedVlanId, hpSwitchLocalMgmtPrivCmdSendLog=hpSwitchLocalMgmtPrivCmdSendLog, PYSNMP_MODULE_ID=hpSwitchAuthorizationMIB, hpSwitchAuthorizationNotificationGrpMIBCompliance=hpSwitchAuthorizationNotificationGrpMIBCompliance, hpSwitchLocalMgmtPrivCmdPriv=hpSwitchLocalMgmtPrivCmdPriv, hpSwitchAutzServicePrimaryMethod=hpSwitchAutzServicePrimaryMethod, hpicfSwitchAuthServerNotifyEnable=hpicfSwitchAuthServerNotifyEnable, hpSwitchLocalMgmtPrivCommandsEntry=hpSwitchLocalMgmtPrivCommandsEntry, hpSwitchAutzServiceEntry=hpSwitchAutzServiceEntry, hpSwitchLocalMgmtPrivGroupIndex=hpSwitchLocalMgmtPrivGroupIndex, hpSwitchAutzServiceCommandsLevel=hpSwitchAutzServiceCommandsLevel, hpicfSwitchAuthorizationObjectsGroup=hpicfSwitchAuthorizationObjectsGroup, hpSwitchAutzRoleGrpCompliance2=hpSwitchAutzRoleGrpCompliance2, hpSwitchAutzServiceType=hpSwitchAutzServiceType, hpSwitchLocalMgmtPrivCmdMatchStr=hpSwitchLocalMgmtPrivCmdMatchStr, hpSwitchAutzUserRoleTunneledNodeServerRedirect=hpSwitchAutzUserRoleTunneledNodeServerRedirect, hpicfSwitchAuthorizationNotificationGroup=hpicfSwitchAuthorizationNotificationGroup, hpSwitchLocalMgmtPrivCmdSequenceIndex=hpSwitchLocalMgmtPrivCmdSequenceIndex, hpSwitchAutzServiceTable=hpSwitchAutzServiceTable, hpSwitchAutzUserRoleDownloadedEnabled=hpSwitchAutzUserRoleDownloadedEnabled, hpSwitchAutzUserRole=hpSwitchAutzUserRole, hpSwitchLocalMgmtPrivCmdStatus=hpSwitchLocalMgmtPrivCmdStatus, hpSwitchAutzUserRoleRowStatus=hpSwitchAutzUserRoleRowStatus, hpSwitchAutzUserRoleEnabled=hpSwitchAutzUserRoleEnabled, hpSwitchLocalMgmtPrivGrpMIBCompliance1=hpSwitchLocalMgmtPrivGrpMIBCompliance1, hpSwitchAutzUserRoleReauthPeriod=hpSwitchAutzUserRoleReauthPeriod, hpSwitchAutzUserRoleGroup=hpSwitchAutzUserRoleGroup, hpSwitchAutzUserRoleGroup1=hpSwitchAutzUserRoleGroup1, hpSwitchAuthorizationMIBCompliance=hpSwitchAuthorizationMIBCompliance, hpicfSwitchAuthServerFail=hpicfSwitchAuthServerFail, hpSwitchAutzUserRoleIngressUserPolicyName=hpSwitchAutzUserRoleIngressUserPolicyName, hpSwitchLocalMgmtPrivGroupStatus=hpSwitchLocalMgmtPrivGroupStatus, hpSwitchAutzUserRoleVlanName=hpSwitchAutzUserRoleVlanName, hpSwitchLocalMgmtPrivGroupsTable=hpSwitchLocalMgmtPrivGroupsTable, hpSwitchAutzUserRoleCaptivePortalProfileName=hpSwitchAutzUserRoleCaptivePortalProfileName, hpSwitchAuthorizationMIBGroups=hpSwitchAuthorizationMIBGroups, hpSwitchAutzLocalMgmtPrivGroup=hpSwitchAutzLocalMgmtPrivGroup, hpSwitchAutzUserRoleTaggedVlanName=hpSwitchAutzUserRoleTaggedVlanName, hpSwitchAutzUserRoleGroup2=hpSwitchAutzUserRoleGroup2, hpSwitchAutzUserRoleName=hpSwitchAutzUserRoleName, hpSwitchLocalMgmtPrivGroupName=hpSwitchLocalMgmtPrivGroupName, hpSwitchAuthConfigObjects=hpSwitchAuthConfigObjects, hpSwitchAutzRoleGrpCompliance3=hpSwitchAutzRoleGrpCompliance3, hpSwitchLocalMgmtPrivCommandsTable=hpSwitchLocalMgmtPrivCommandsTable, hpSwitchAuthorizationConfigGroup=hpSwitchAuthorizationConfigGroup, hpicfSwitchAuthServerType=hpicfSwitchAuthServerType, hpSwitchLocalMgmtPrivGrpMIBCompliance=hpSwitchLocalMgmtPrivGrpMIBCompliance, HpAutzUserRoleName=HpAutzUserRoleName, hpSwitchAuthorizationMIBCompliances=hpSwitchAuthorizationMIBCompliances, hpSwitchAuthorizationConfig=hpSwitchAuthorizationConfig, hpSwitchAutzUserRoleEntry=hpSwitchAutzUserRoleEntry, hpSwitchAutzLocalMgmtPrivGroup1=hpSwitchAutzLocalMgmtPrivGroup1, hpSwitchAuthorizationMIB=hpSwitchAuthorizationMIB, hpSwitchAutzRoleGrpCompliance=hpSwitchAutzRoleGrpCompliance, hpSwitchAutzServiceSecondaryMethod=hpSwitchAutzServiceSecondaryMethod, hpSwitchAuthLocalPrivConfigObjects=hpSwitchAuthLocalPrivConfigObjects, hpSwitchAutzUserRoleType=hpSwitchAutzUserRoleType)
