#
# PySNMP MIB module AGGREGATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AGGREGATE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:00:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
OwnerString, = mibBuilder.importSymbols("RMON-MIB", "OwnerString")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
IpAddress, Integer32, ObjectIdentity, ModuleIdentity, Opaque, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Gauge32, TimeTicks, Bits, MibIdentifier, experimental, iso, NotificationType, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Integer32", "ObjectIdentity", "ModuleIdentity", "Opaque", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Gauge32", "TimeTicks", "Bits", "MibIdentifier", "experimental", "iso", "NotificationType", "Unsigned32")
RowStatus, TextualConvention, DisplayString, StorageType = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString", "StorageType")
aggrMIB = ModuleIdentity((1, 3, 6, 1, 3, 123))
aggrMIB.setRevisions(('2006-04-27 00:00',))
if mibBuilder.loadTexts: aggrMIB.setLastUpdated('200604270000Z')
if mibBuilder.loadTexts: aggrMIB.setOrganization('Cyber Solutions Inc. NetMan Working Group')
class AggrMOErrorStatus(TextualConvention, Opaque):
    status = 'current'
    subtypeSpec = Opaque.subtypeSpec + ValueSizeConstraint(0, 1024)

class AggrMOValue(TextualConvention, Opaque):
    status = 'current'
    subtypeSpec = Opaque.subtypeSpec + ValueSizeConstraint(0, 1024)

class AggrMOCompressedValue(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1024)

aggrCtlTable = MibTable((1, 3, 6, 1, 3, 123, 1), )
if mibBuilder.loadTexts: aggrCtlTable.setStatus('current')
aggrCtlEntry = MibTableRow((1, 3, 6, 1, 3, 123, 1, 1), ).setIndexNames((0, "AGGREGATE-MIB", "aggrCtlEntryID"))
if mibBuilder.loadTexts: aggrCtlEntry.setStatus('current')
aggrCtlEntryID = MibTableColumn((1, 3, 6, 1, 3, 123, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: aggrCtlEntryID.setStatus('current')
aggrCtlMOIndex = MibTableColumn((1, 3, 6, 1, 3, 123, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aggrCtlMOIndex.setStatus('current')
aggrCtlMODescr = MibTableColumn((1, 3, 6, 1, 3, 123, 1, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aggrCtlMODescr.setStatus('current')
aggrCtlCompressionAlgorithm = MibTableColumn((1, 3, 6, 1, 3, 123, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("deflate", 2))).clone('none')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aggrCtlCompressionAlgorithm.setStatus('current')
aggrCtlEntryOwner = MibTableColumn((1, 3, 6, 1, 3, 123, 1, 1, 5), OwnerString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aggrCtlEntryOwner.setStatus('current')
aggrCtlEntryStorageType = MibTableColumn((1, 3, 6, 1, 3, 123, 1, 1, 6), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aggrCtlEntryStorageType.setStatus('current')
aggrCtlEntryStatus = MibTableColumn((1, 3, 6, 1, 3, 123, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aggrCtlEntryStatus.setStatus('current')
aggrMOTable = MibTable((1, 3, 6, 1, 3, 123, 2), )
if mibBuilder.loadTexts: aggrMOTable.setStatus('current')
aggrMOEntry = MibTableRow((1, 3, 6, 1, 3, 123, 2, 1), ).setIndexNames((0, "AGGREGATE-MIB", "aggrMOEntryID"), (0, "AGGREGATE-MIB", "aggrMOEntryMOID"))
if mibBuilder.loadTexts: aggrMOEntry.setStatus('current')
aggrMOEntryID = MibTableColumn((1, 3, 6, 1, 3, 123, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: aggrMOEntryID.setStatus('current')
aggrMOEntryMOID = MibTableColumn((1, 3, 6, 1, 3, 123, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: aggrMOEntryMOID.setStatus('current')
aggrMOInstance = MibTableColumn((1, 3, 6, 1, 3, 123, 2, 1, 3), ObjectIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aggrMOInstance.setStatus('current')
aggrMODescr = MibTableColumn((1, 3, 6, 1, 3, 123, 2, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aggrMODescr.setStatus('current')
aggrMOEntryStorageType = MibTableColumn((1, 3, 6, 1, 3, 123, 2, 1, 5), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aggrMOEntryStorageType.setStatus('current')
aggrMOEntryStatus = MibTableColumn((1, 3, 6, 1, 3, 123, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aggrMOEntryStatus.setStatus('current')
aggrDataTable = MibTable((1, 3, 6, 1, 3, 123, 3), )
if mibBuilder.loadTexts: aggrDataTable.setStatus('current')
aggrDataEntry = MibTableRow((1, 3, 6, 1, 3, 123, 3, 1), ).setIndexNames((0, "AGGREGATE-MIB", "aggrCtlEntryID"))
if mibBuilder.loadTexts: aggrDataEntry.setStatus('current')
aggrDataRecord = MibTableColumn((1, 3, 6, 1, 3, 123, 3, 1, 1), AggrMOValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aggrDataRecord.setStatus('current')
aggrDataRecordCompressed = MibTableColumn((1, 3, 6, 1, 3, 123, 3, 1, 2), AggrMOCompressedValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aggrDataRecordCompressed.setStatus('current')
aggrDataErrorRecord = MibTableColumn((1, 3, 6, 1, 3, 123, 3, 1, 3), AggrMOErrorStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aggrDataErrorRecord.setStatus('current')
aggrConformance = MibIdentifier((1, 3, 6, 1, 3, 123, 4))
aggrGroups = MibIdentifier((1, 3, 6, 1, 3, 123, 4, 1))
aggrCompliances = MibIdentifier((1, 3, 6, 1, 3, 123, 4, 2))
aggrMibCompliance = ModuleCompliance((1, 3, 6, 1, 3, 123, 4, 2, 1)).setObjects(("AGGREGATE-MIB", "aggrMibBasicGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aggrMibCompliance = aggrMibCompliance.setStatus('current')
aggrMibBasicGroup = ObjectGroup((1, 3, 6, 1, 3, 123, 4, 1, 1)).setObjects(("AGGREGATE-MIB", "aggrCtlMOIndex"), ("AGGREGATE-MIB", "aggrCtlMODescr"), ("AGGREGATE-MIB", "aggrCtlCompressionAlgorithm"), ("AGGREGATE-MIB", "aggrCtlEntryOwner"), ("AGGREGATE-MIB", "aggrCtlEntryStorageType"), ("AGGREGATE-MIB", "aggrCtlEntryStatus"), ("AGGREGATE-MIB", "aggrMOInstance"), ("AGGREGATE-MIB", "aggrMODescr"), ("AGGREGATE-MIB", "aggrMOEntryStorageType"), ("AGGREGATE-MIB", "aggrMOEntryStatus"), ("AGGREGATE-MIB", "aggrDataRecord"), ("AGGREGATE-MIB", "aggrDataRecordCompressed"), ("AGGREGATE-MIB", "aggrDataErrorRecord"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aggrMibBasicGroup = aggrMibBasicGroup.setStatus('current')
mibBuilder.exportSymbols("AGGREGATE-MIB", aggrMOEntryStorageType=aggrMOEntryStorageType, aggrDataRecordCompressed=aggrDataRecordCompressed, aggrMODescr=aggrMODescr, aggrDataEntry=aggrDataEntry, aggrCtlEntryOwner=aggrCtlEntryOwner, aggrCtlEntry=aggrCtlEntry, aggrDataRecord=aggrDataRecord, aggrCtlEntryStorageType=aggrCtlEntryStorageType, aggrMOEntryMOID=aggrMOEntryMOID, aggrCtlEntryStatus=aggrCtlEntryStatus, aggrGroups=aggrGroups, aggrMibBasicGroup=aggrMibBasicGroup, aggrDataTable=aggrDataTable, AggrMOErrorStatus=AggrMOErrorStatus, aggrCtlCompressionAlgorithm=aggrCtlCompressionAlgorithm, aggrMOEntryID=aggrMOEntryID, PYSNMP_MODULE_ID=aggrMIB, aggrDataErrorRecord=aggrDataErrorRecord, aggrCtlMOIndex=aggrCtlMOIndex, aggrCtlEntryID=aggrCtlEntryID, aggrMOEntry=aggrMOEntry, aggrMibCompliance=aggrMibCompliance, aggrMOTable=aggrMOTable, aggrMOInstance=aggrMOInstance, aggrCtlMODescr=aggrCtlMODescr, aggrMOEntryStatus=aggrMOEntryStatus, aggrCtlTable=aggrCtlTable, aggrConformance=aggrConformance, aggrCompliances=aggrCompliances, AggrMOCompressedValue=AggrMOCompressedValue, aggrMIB=aggrMIB, AggrMOValue=AggrMOValue)
