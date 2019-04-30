#
# PySNMP MIB module ENTERASYS-MAU-MIB-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ENTERASYS-MAU-MIB-EXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:49:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
ifMauIfIndex, = mibBuilder.importSymbols("MAU-MIB", "ifMauIfIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
TimeTicks, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64, Integer32, iso, ModuleIdentity, NotificationType, ObjectIdentity, Gauge32, MibIdentifier, Counter32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64", "Integer32", "iso", "ModuleIdentity", "NotificationType", "ObjectIdentity", "Gauge32", "MibIdentifier", "Counter32", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
etsysMauMibExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 59))
etsysMauMibExtMIB.setRevisions(('2006-05-09 11:30', '2006-02-16 19:18', '2005-02-07 15:05',))
if mibBuilder.loadTexts: etsysMauMibExtMIB.setLastUpdated('200605091130Z')
if mibBuilder.loadTexts: etsysMauMibExtMIB.setOrganization('Enterasys Networks, Inc.')
etsysMauMibExtObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 1))
etsysMauMibExtBasic = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 1, 1))
etsysIfMauExtMDIXTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 1, 1, 1), )
if mibBuilder.loadTexts: etsysIfMauExtMDIXTable.setStatus('current')
etsysIfMauExtMDIXEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 1, 1, 1, 1), ).setIndexNames((0, "MAU-MIB", "ifMauIfIndex"))
if mibBuilder.loadTexts: etsysIfMauExtMDIXEntry.setStatus('current')
etsysIfMauExtMDIXStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("mdix", 2), ("mdi", 3))).clone('auto')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysIfMauExtMDIXStatus.setStatus('current')
etsysIfMauExtMasterSlaveTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 1, 1, 2), )
if mibBuilder.loadTexts: etsysIfMauExtMasterSlaveTable.setStatus('deprecated')
etsysIfMauExtMasterSlaveEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 1, 1, 2, 1), ).setIndexNames((0, "MAU-MIB", "ifMauIfIndex"))
if mibBuilder.loadTexts: etsysIfMauExtMasterSlaveEntry.setStatus('deprecated')
etsysIfMauExtMasterSlaveStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("master", 1), ("slave", 2))).clone('slave')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysIfMauExtMasterSlaveStatus.setStatus('deprecated')
etsysMauMibExtConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 2))
etsysMauMibExtGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 2, 1))
etsysMauMibExtCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 2, 2))
etsysMauMibExtMDIXGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 2, 1, 1)).setObjects(("ENTERASYS-MAU-MIB-EXT-MIB", "etsysIfMauExtMDIXStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMauMibExtMDIXGroup = etsysMauMibExtMDIXGroup.setStatus('current')
etsysMauMibExtMasterSlaveGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 2, 1, 2)).setObjects(("ENTERASYS-MAU-MIB-EXT-MIB", "etsysIfMauExtMasterSlaveStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMauMibExtMasterSlaveGroup = etsysMauMibExtMasterSlaveGroup.setStatus('deprecated')
etsysMauMibExtMDIXCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 2, 2, 1)).setObjects(("ENTERASYS-MAU-MIB-EXT-MIB", "etsysMauMibExtMDIXGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMauMibExtMDIXCompliance = etsysMauMibExtMDIXCompliance.setStatus('current')
etsysMauMibExtMasterSlaveCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 2, 2, 2)).setObjects(("ENTERASYS-MAU-MIB-EXT-MIB", "etsysMauMibExtMasterSlaveGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMauMibExtMasterSlaveCompliance = etsysMauMibExtMasterSlaveCompliance.setStatus('deprecated')
mibBuilder.exportSymbols("ENTERASYS-MAU-MIB-EXT-MIB", PYSNMP_MODULE_ID=etsysMauMibExtMIB, etsysIfMauExtMasterSlaveStatus=etsysIfMauExtMasterSlaveStatus, etsysMauMibExtMDIXCompliance=etsysMauMibExtMDIXCompliance, etsysIfMauExtMasterSlaveTable=etsysIfMauExtMasterSlaveTable, etsysIfMauExtMDIXStatus=etsysIfMauExtMDIXStatus, etsysMauMibExtMDIXGroup=etsysMauMibExtMDIXGroup, etsysMauMibExtMIB=etsysMauMibExtMIB, etsysMauMibExtConformance=etsysMauMibExtConformance, etsysMauMibExtMasterSlaveGroup=etsysMauMibExtMasterSlaveGroup, etsysMauMibExtGroups=etsysMauMibExtGroups, etsysMauMibExtObjects=etsysMauMibExtObjects, etsysMauMibExtMasterSlaveCompliance=etsysMauMibExtMasterSlaveCompliance, etsysIfMauExtMDIXTable=etsysIfMauExtMDIXTable, etsysMauMibExtBasic=etsysMauMibExtBasic, etsysIfMauExtMDIXEntry=etsysIfMauExtMDIXEntry, etsysIfMauExtMasterSlaveEntry=etsysIfMauExtMasterSlaveEntry, etsysMauMibExtCompliances=etsysMauMibExtCompliances)
