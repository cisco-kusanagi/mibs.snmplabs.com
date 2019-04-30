#
# PySNMP MIB module XEDIA-DIALBACKUP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/XEDIA-DIALBACKUP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:36:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Integer32, ObjectIdentity, IpAddress, ModuleIdentity, NotificationType, Unsigned32, MibIdentifier, Counter64, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, iso, Counter32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ObjectIdentity", "IpAddress", "ModuleIdentity", "NotificationType", "Unsigned32", "MibIdentifier", "Counter64", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "iso", "Counter32", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
xediaMibs, = mibBuilder.importSymbols("XEDIA-REG", "xediaMibs")
xediaDialBackupMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 838, 3, 36))
if mibBuilder.loadTexts: xediaDialBackupMIB.setLastUpdated('9908112155Z')
if mibBuilder.loadTexts: xediaDialBackupMIB.setOrganization('Xedia Corp.')
dialBackupObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 36, 1))
dialBackupConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 36, 2))
dialBackupConfigurationTable = MibTable((1, 3, 6, 1, 4, 1, 838, 3, 36, 1, 1), )
if mibBuilder.loadTexts: dialBackupConfigurationTable.setStatus('current')
dialBackupConfigurationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 838, 3, 36, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: dialBackupConfigurationEntry.setStatus('current')
dialBackupPrimaryInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 36, 1, 1, 1, 1), DisplayString().clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dialBackupPrimaryInterface.setStatus('current')
dialBackupFailoverTime = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 36, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: dialBackupFailoverTime.setStatus('current')
dialBackupFailbackTime = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 36, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: dialBackupFailbackTime.setStatus('current')
dialBackupStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 36, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dialBackupStatus.setStatus('current')
dialBackupCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 36, 2, 1))
dialBackupGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 36, 2, 2))
dialBackupCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 838, 3, 36, 2, 1, 1)).setObjects(("XEDIA-DIALBACKUP-MIB", "dialBackupAllGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dialBackupCompliance = dialBackupCompliance.setStatus('current')
dialBackupAllGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 838, 3, 36, 2, 2, 1)).setObjects(("XEDIA-DIALBACKUP-MIB", "dialBackupPrimaryInterface"), ("XEDIA-DIALBACKUP-MIB", "dialBackupFailoverTime"), ("XEDIA-DIALBACKUP-MIB", "dialBackupFailbackTime"), ("XEDIA-DIALBACKUP-MIB", "dialBackupStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dialBackupAllGroup = dialBackupAllGroup.setStatus('current')
mibBuilder.exportSymbols("XEDIA-DIALBACKUP-MIB", dialBackupFailbackTime=dialBackupFailbackTime, dialBackupConformance=dialBackupConformance, dialBackupCompliances=dialBackupCompliances, xediaDialBackupMIB=xediaDialBackupMIB, dialBackupConfigurationEntry=dialBackupConfigurationEntry, dialBackupPrimaryInterface=dialBackupPrimaryInterface, dialBackupFailoverTime=dialBackupFailoverTime, dialBackupAllGroup=dialBackupAllGroup, dialBackupConfigurationTable=dialBackupConfigurationTable, PYSNMP_MODULE_ID=xediaDialBackupMIB, dialBackupCompliance=dialBackupCompliance, dialBackupGroups=dialBackupGroups, dialBackupObjects=dialBackupObjects, dialBackupStatus=dialBackupStatus)
