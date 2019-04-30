#
# PySNMP MIB module ENERGY-OBJECT-CONTEXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ENERGY-OBJECT-CONTEXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:48:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
IANAEnergyRelationship, = mibBuilder.importSymbols("IANA-ENERGY-RELATION-MIB", "IANAEnergyRelationship")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
NotificationType, ObjectIdentity, iso, Gauge32, TimeTicks, Bits, Counter32, Counter64, mib_2, IpAddress, MibIdentifier, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ObjectIdentity", "iso", "Gauge32", "TimeTicks", "Bits", "Counter32", "Counter64", "mib-2", "IpAddress", "MibIdentifier", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Unsigned32")
MacAddress, DisplayString, TruthValue, TextualConvention, RowStatus, StorageType = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "DisplayString", "TruthValue", "TextualConvention", "RowStatus", "StorageType")
UUIDorZero, = mibBuilder.importSymbols("UUID-TC-MIB", "UUIDorZero")
energyObjectContextMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 231))
energyObjectContextMIB.setRevisions(('2015-02-09 00:00',))
if mibBuilder.loadTexts: energyObjectContextMIB.setLastUpdated('201502090000Z')
if mibBuilder.loadTexts: energyObjectContextMIB.setOrganization('IETF EMAN Working Group')
energyObjectContextMIBNotifs = MibIdentifier((1, 3, 6, 1, 2, 1, 231, 0))
energyObjectContextMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 231, 1))
energyObjectContextMIBConform = MibIdentifier((1, 3, 6, 1, 2, 1, 231, 2))
class PethPsePortIndexOrZero(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class PethPsePortGroupIndexOrZero(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class LldpPortNumberOrZero(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4096)

class EnergyObjectKeywordList(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 2048)

eoTable = MibTable((1, 3, 6, 1, 2, 1, 231, 1, 1), )
if mibBuilder.loadTexts: eoTable.setStatus('current')
eoEntry = MibTableRow((1, 3, 6, 1, 2, 1, 231, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: eoEntry.setStatus('current')
eoEthPortIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 231, 1, 1, 1, 1), PethPsePortIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eoEthPortIndex.setStatus('current')
eoEthPortGrpIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 231, 1, 1, 1, 2), PethPsePortGroupIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eoEthPortGrpIndex.setStatus('current')
eoLldpPortNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 231, 1, 1, 1, 3), LldpPortNumberOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eoLldpPortNumber.setStatus('current')
eoMgmtMacAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 231, 1, 1, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eoMgmtMacAddress.setStatus('current')
eoMgmtAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 231, 1, 1, 1, 5), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eoMgmtAddressType.setStatus('current')
eoMgmtAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 231, 1, 1, 1, 6), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eoMgmtAddress.setStatus('current')
eoMgmtDNSName = MibTableColumn((1, 3, 6, 1, 2, 1, 231, 1, 1, 1, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eoMgmtDNSName.setStatus('current')
eoDomainName = MibTableColumn((1, 3, 6, 1, 2, 1, 231, 1, 1, 1, 8), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eoDomainName.setStatus('current')
eoRoleDescription = MibTableColumn((1, 3, 6, 1, 2, 1, 231, 1, 1, 1, 9), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eoRoleDescription.setStatus('current')
eoKeywords = MibTableColumn((1, 3, 6, 1, 2, 1, 231, 1, 1, 1, 10), EnergyObjectKeywordList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eoKeywords.setStatus('current')
eoImportance = MibTableColumn((1, 3, 6, 1, 2, 1, 231, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eoImportance.setStatus('current')
eoPowerCategory = MibTableColumn((1, 3, 6, 1, 2, 1, 231, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("consumer", 0), ("producer", 1), ("meter", 2), ("distributor", 3), ("store", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eoPowerCategory.setStatus('current')
eoAlternateKey = MibTableColumn((1, 3, 6, 1, 2, 1, 231, 1, 1, 1, 13), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eoAlternateKey.setStatus('current')
eoPowerInterfaceType = MibTableColumn((1, 3, 6, 1, 2, 1, 231, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("inlet", 0), ("outlet", 1), ("both", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eoPowerInterfaceType.setStatus('current')
eoRelationTable = MibTable((1, 3, 6, 1, 2, 1, 231, 1, 2), )
if mibBuilder.loadTexts: eoRelationTable.setStatus('current')
eoRelationEntry = MibTableRow((1, 3, 6, 1, 2, 1, 231, 1, 2, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "ENERGY-OBJECT-CONTEXT-MIB", "eoRelationIndex"))
if mibBuilder.loadTexts: eoRelationEntry.setStatus('current')
eoRelationIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 231, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: eoRelationIndex.setStatus('current')
eoRelationID = MibTableColumn((1, 3, 6, 1, 2, 1, 231, 1, 2, 1, 2), UUIDorZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eoRelationID.setStatus('current')
eoRelationship = MibTableColumn((1, 3, 6, 1, 2, 1, 231, 1, 2, 1, 3), IANAEnergyRelationship()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eoRelationship.setStatus('current')
eoRelationStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 231, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eoRelationStatus.setStatus('current')
eoRelationStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 231, 1, 2, 1, 5), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eoRelationStorageType.setStatus('current')
energyObjectContextMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 231, 2, 1))
energyObjectContextMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 231, 2, 2))
energyObjectContextMIBFullCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 231, 2, 1, 1)).setObjects(("ENERGY-OBJECT-CONTEXT-MIB", "energyObjectContextMIBTableGroup"), ("ENERGY-OBJECT-CONTEXT-MIB", "energyObjectRelationTableGroup"), ("ENERGY-OBJECT-CONTEXT-MIB", "energyObjectOptionalMIBTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    energyObjectContextMIBFullCompliance = energyObjectContextMIBFullCompliance.setStatus('current')
energyObjectContextMIBReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 231, 2, 1, 2)).setObjects(("ENERGY-OBJECT-CONTEXT-MIB", "energyObjectContextMIBTableGroup"), ("ENERGY-OBJECT-CONTEXT-MIB", "energyObjectRelationTableGroup"), ("ENERGY-OBJECT-CONTEXT-MIB", "energyObjectOptionalMIBTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    energyObjectContextMIBReadOnlyCompliance = energyObjectContextMIBReadOnlyCompliance.setStatus('current')
energyObjectContextMIBTableGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 231, 2, 2, 1)).setObjects(("ENERGY-OBJECT-CONTEXT-MIB", "eoDomainName"), ("ENERGY-OBJECT-CONTEXT-MIB", "eoRoleDescription"), ("ENERGY-OBJECT-CONTEXT-MIB", "eoAlternateKey"), ("ENERGY-OBJECT-CONTEXT-MIB", "eoKeywords"), ("ENERGY-OBJECT-CONTEXT-MIB", "eoImportance"), ("ENERGY-OBJECT-CONTEXT-MIB", "eoPowerCategory"), ("ENERGY-OBJECT-CONTEXT-MIB", "eoPowerInterfaceType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    energyObjectContextMIBTableGroup = energyObjectContextMIBTableGroup.setStatus('current')
energyObjectOptionalMIBTableGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 231, 2, 2, 2)).setObjects(("ENERGY-OBJECT-CONTEXT-MIB", "eoEthPortIndex"), ("ENERGY-OBJECT-CONTEXT-MIB", "eoEthPortGrpIndex"), ("ENERGY-OBJECT-CONTEXT-MIB", "eoLldpPortNumber"), ("ENERGY-OBJECT-CONTEXT-MIB", "eoMgmtMacAddress"), ("ENERGY-OBJECT-CONTEXT-MIB", "eoMgmtAddressType"), ("ENERGY-OBJECT-CONTEXT-MIB", "eoMgmtAddress"), ("ENERGY-OBJECT-CONTEXT-MIB", "eoMgmtDNSName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    energyObjectOptionalMIBTableGroup = energyObjectOptionalMIBTableGroup.setStatus('current')
energyObjectRelationTableGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 231, 2, 2, 3)).setObjects(("ENERGY-OBJECT-CONTEXT-MIB", "eoRelationID"), ("ENERGY-OBJECT-CONTEXT-MIB", "eoRelationship"), ("ENERGY-OBJECT-CONTEXT-MIB", "eoRelationStatus"), ("ENERGY-OBJECT-CONTEXT-MIB", "eoRelationStorageType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    energyObjectRelationTableGroup = energyObjectRelationTableGroup.setStatus('current')
mibBuilder.exportSymbols("ENERGY-OBJECT-CONTEXT-MIB", energyObjectContextMIBTableGroup=energyObjectContextMIBTableGroup, PYSNMP_MODULE_ID=energyObjectContextMIB, eoDomainName=eoDomainName, eoRelationTable=eoRelationTable, energyObjectRelationTableGroup=energyObjectRelationTableGroup, LldpPortNumberOrZero=LldpPortNumberOrZero, eoAlternateKey=eoAlternateKey, eoRelationIndex=eoRelationIndex, eoRelationStorageType=eoRelationStorageType, EnergyObjectKeywordList=EnergyObjectKeywordList, energyObjectContextMIBGroups=energyObjectContextMIBGroups, eoMgmtAddress=eoMgmtAddress, energyObjectContextMIBReadOnlyCompliance=energyObjectContextMIBReadOnlyCompliance, eoMgmtMacAddress=eoMgmtMacAddress, eoImportance=eoImportance, eoRoleDescription=eoRoleDescription, eoEthPortGrpIndex=eoEthPortGrpIndex, eoRelationship=eoRelationship, energyObjectContextMIBCompliances=energyObjectContextMIBCompliances, energyObjectContextMIBConform=energyObjectContextMIBConform, eoEntry=eoEntry, energyObjectContextMIB=energyObjectContextMIB, PethPsePortIndexOrZero=PethPsePortIndexOrZero, eoMgmtDNSName=eoMgmtDNSName, energyObjectContextMIBObjects=energyObjectContextMIBObjects, eoEthPortIndex=eoEthPortIndex, energyObjectContextMIBFullCompliance=energyObjectContextMIBFullCompliance, eoMgmtAddressType=eoMgmtAddressType, eoPowerCategory=eoPowerCategory, energyObjectOptionalMIBTableGroup=energyObjectOptionalMIBTableGroup, eoRelationID=eoRelationID, eoRelationStatus=eoRelationStatus, eoPowerInterfaceType=eoPowerInterfaceType, PethPsePortGroupIndexOrZero=PethPsePortGroupIndexOrZero, eoLldpPortNumber=eoLldpPortNumber, energyObjectContextMIBNotifs=energyObjectContextMIBNotifs, eoKeywords=eoKeywords, eoRelationEntry=eoRelationEntry, eoTable=eoTable)
