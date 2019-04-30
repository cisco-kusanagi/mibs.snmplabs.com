#
# PySNMP MIB module XEDIA-IPBACKUP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/XEDIA-IPBACKUP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:36:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, NotificationType, Unsigned32, Integer32, TimeTicks, IpAddress, Gauge32, iso, ModuleIdentity, Counter32, Counter64, Bits, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "NotificationType", "Unsigned32", "Integer32", "TimeTicks", "IpAddress", "Gauge32", "iso", "ModuleIdentity", "Counter32", "Counter64", "Bits", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
xediaMibs, = mibBuilder.importSymbols("XEDIA-REG", "xediaMibs")
xediaIpBackupMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 838, 3, 15))
if mibBuilder.loadTexts: xediaIpBackupMIB.setLastUpdated('9802232155Z')
if mibBuilder.loadTexts: xediaIpBackupMIB.setOrganization('Xedia Corp.')
class BackupId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 255)

xipbackupObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 15, 1))
xipbackupConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 15, 2))
xipbackupGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 15, 1, 1))
xipbackupAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 838, 3, 15, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xipbackupAdminStatus.setStatus('current')
xipbackupBridgeAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 838, 3, 15, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xipbackupBridgeAdminStatus.setStatus('current')
xipbackupInstTable = MibTable((1, 3, 6, 1, 4, 1, 838, 3, 15, 1, 2), )
if mibBuilder.loadTexts: xipbackupInstTable.setStatus('current')
xipbackupInstEntry = MibTableRow((1, 3, 6, 1, 4, 1, 838, 3, 15, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "XEDIA-IPBACKUP-MIB", "xipbackupInstId"))
if mibBuilder.loadTexts: xipbackupInstEntry.setStatus('current')
xipbackupInstId = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 15, 1, 2, 1, 1), BackupId())
if mibBuilder.loadTexts: xipbackupInstId.setStatus('current')
xipbackupInstTrackIp = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 15, 1, 2, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xipbackupInstTrackIp.setStatus('current')
xipbackupInstInitializeCode = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 15, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("ready", 1), ("globalDisabled", 2), ("instanceDisabled", 3), ("rowStatusNotActive", 4), ("noAssociatedIpAddr", 5), ("noAddressOnSubnet", 6), ("trackedIpDown", 7), ("interfaceDown", 8), ("bridgeDown", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xipbackupInstInitializeCode.setStatus('current')
xipbackupCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 15, 2, 1))
xipbackupGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 15, 2, 2))
xipbackupCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 838, 3, 15, 2, 1, 1)).setObjects(("XEDIA-IPBACKUP-MIB", "xipbackupAllGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xipbackupCompliance = xipbackupCompliance.setStatus('current')
xipbackupAllGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 838, 3, 15, 2, 2, 1)).setObjects(("XEDIA-IPBACKUP-MIB", "xipbackupAdminStatus"), ("XEDIA-IPBACKUP-MIB", "xipbackupBridgeAdminStatus"), ("XEDIA-IPBACKUP-MIB", "xipbackupInstTrackIp"), ("XEDIA-IPBACKUP-MIB", "xipbackupInstInitializeCode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xipbackupAllGroup = xipbackupAllGroup.setStatus('current')
mibBuilder.exportSymbols("XEDIA-IPBACKUP-MIB", xipbackupGroups=xipbackupGroups, xipbackupInstTable=xipbackupInstTable, xipbackupInstTrackIp=xipbackupInstTrackIp, xipbackupCompliance=xipbackupCompliance, xipbackupBridgeAdminStatus=xipbackupBridgeAdminStatus, BackupId=BackupId, xipbackupObjects=xipbackupObjects, xipbackupAllGroup=xipbackupAllGroup, xipbackupAdminStatus=xipbackupAdminStatus, xipbackupGeneral=xipbackupGeneral, xipbackupConformance=xipbackupConformance, PYSNMP_MODULE_ID=xediaIpBackupMIB, xediaIpBackupMIB=xediaIpBackupMIB, xipbackupInstEntry=xipbackupInstEntry, xipbackupInstInitializeCode=xipbackupInstInitializeCode, xipbackupInstId=xipbackupInstId, xipbackupCompliances=xipbackupCompliances)
