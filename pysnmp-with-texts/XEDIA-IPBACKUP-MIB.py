#
# PySNMP MIB module XEDIA-IPBACKUP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/XEDIA-IPBACKUP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:42:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, TimeTicks, MibIdentifier, Unsigned32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter64, IpAddress, Counter32, Integer32, ObjectIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "TimeTicks", "MibIdentifier", "Unsigned32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter64", "IpAddress", "Counter32", "Integer32", "ObjectIdentity", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
xediaMibs, = mibBuilder.importSymbols("XEDIA-REG", "xediaMibs")
xediaIpBackupMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 838, 3, 15))
if mibBuilder.loadTexts: xediaIpBackupMIB.setLastUpdated('9802232155Z')
if mibBuilder.loadTexts: xediaIpBackupMIB.setOrganization('Xedia Corp.')
if mibBuilder.loadTexts: xediaIpBackupMIB.setContactInfo('support@xedia.com')
if mibBuilder.loadTexts: xediaIpBackupMIB.setDescription('This module defines additional objects for management of IP Backup in Xedia devices, above and beyond what is defined in the for the VRRP (or other implemented backup procedures).')
class BackupId(TextualConvention, Integer32):
    description = "A unique number that serves to identify an instance of IP backup. This is equivalent to the type 'VrId' defined for VRRP."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 255)

xipbackupObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 15, 1))
xipbackupConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 15, 2))
xipbackupGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 15, 1, 1))
xipbackupAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 838, 3, 15, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xipbackupAdminStatus.setStatus('current')
if mibBuilder.loadTexts: xipbackupAdminStatus.setDescription("The administrative status of IP Backup for the IP router. It is the desired state of IP Backup for the router. The value 'enabled(1)' indicates that the IP Backup process should be active in the router, while 'disabled(2)' indicates that IP Backup should not be active for the router.")
xipbackupBridgeAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 838, 3, 15, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xipbackupBridgeAdminStatus.setStatus('current')
if mibBuilder.loadTexts: xipbackupBridgeAdminStatus.setDescription("The administrative status of IP Backup for the bridge. It is the desired state of IP Backup for the bridge. The value 'enabled(1)' indicates that the IP Backup process should be active in the router, while 'disabled(2)' indicates that IP Backup should not be active for the bridge. The bridge will not forward frames if this value is enabled unless it has achieved the master state through the IP Backup protocol.")
xipbackupInstTable = MibTable((1, 3, 6, 1, 4, 1, 838, 3, 15, 1, 2), )
if mibBuilder.loadTexts: xipbackupInstTable.setStatus('current')
if mibBuilder.loadTexts: xipbackupInstTable.setDescription('The information associated with a backup instance. This typically augments the vrrpOperTable.')
xipbackupInstEntry = MibTableRow((1, 3, 6, 1, 4, 1, 838, 3, 15, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "XEDIA-IPBACKUP-MIB", "xipbackupInstId"))
if mibBuilder.loadTexts: xipbackupInstEntry.setStatus('current')
if mibBuilder.loadTexts: xipbackupInstEntry.setDescription('An entry in the table, containing the operational characteristics of a backup instance. A given backup instance is identifed by a combination of the IF index and instance ID. This table typically augments the VRRP vrrpOperTable where vrid = instance ID.')
xipbackupInstId = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 15, 1, 2, 1, 1), BackupId())
if mibBuilder.loadTexts: xipbackupInstId.setStatus('current')
if mibBuilder.loadTexts: xipbackupInstId.setDescription('This object contains the backup instance identifier.')
xipbackupInstTrackIp = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 15, 1, 2, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xipbackupInstTrackIp.setStatus('current')
if mibBuilder.loadTexts: xipbackupInstTrackIp.setDescription("An IP address to be 'tracked' by this backup instance. If this value is set, a backup instance (virtual router) cannot become Master if this interface is not up.")
xipbackupInstInitializeCode = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 15, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("ready", 1), ("globalDisabled", 2), ("instanceDisabled", 3), ("rowStatusNotActive", 4), ("noAssociatedIpAddr", 5), ("noAddressOnSubnet", 6), ("trackedIpDown", 7), ("interfaceDown", 8), ("bridgeDown", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xipbackupInstInitializeCode.setStatus('current')
if mibBuilder.loadTexts: xipbackupInstInitializeCode.setDescription("The reason, if any, that this virtual router has not progressed past the Initialize state. If multiple reasons, are present, only one value is shown and correcting that condition or configuration will reveal the remaining reason(s). If the virtual router may enter the Master or Backup state, the value shown is 'ready'.")
xipbackupCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 15, 2, 1))
xipbackupGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 15, 2, 2))
xipbackupCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 838, 3, 15, 2, 1, 1)).setObjects(("XEDIA-IPBACKUP-MIB", "xipbackupAllGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xipbackupCompliance = xipbackupCompliance.setStatus('current')
if mibBuilder.loadTexts: xipbackupCompliance.setDescription('The compliance statement for all agents that support this MIB. A compliant agent implements all objects defined in this MIB.')
xipbackupAllGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 838, 3, 15, 2, 2, 1)).setObjects(("XEDIA-IPBACKUP-MIB", "xipbackupAdminStatus"), ("XEDIA-IPBACKUP-MIB", "xipbackupBridgeAdminStatus"), ("XEDIA-IPBACKUP-MIB", "xipbackupInstTrackIp"), ("XEDIA-IPBACKUP-MIB", "xipbackupInstInitializeCode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xipbackupAllGroup = xipbackupAllGroup.setStatus('current')
if mibBuilder.loadTexts: xipbackupAllGroup.setDescription('The set of all accessible objects in this MIB.')
mibBuilder.exportSymbols("XEDIA-IPBACKUP-MIB", xipbackupBridgeAdminStatus=xipbackupBridgeAdminStatus, xipbackupGeneral=xipbackupGeneral, xipbackupAdminStatus=xipbackupAdminStatus, xipbackupInstInitializeCode=xipbackupInstInitializeCode, xipbackupInstTable=xipbackupInstTable, BackupId=BackupId, xipbackupObjects=xipbackupObjects, xipbackupInstEntry=xipbackupInstEntry, xipbackupCompliance=xipbackupCompliance, xipbackupAllGroup=xipbackupAllGroup, PYSNMP_MODULE_ID=xediaIpBackupMIB, xipbackupGroups=xipbackupGroups, xipbackupInstTrackIp=xipbackupInstTrackIp, xipbackupCompliances=xipbackupCompliances, xipbackupConformance=xipbackupConformance, xediaIpBackupMIB=xediaIpBackupMIB, xipbackupInstId=xipbackupInstId)
