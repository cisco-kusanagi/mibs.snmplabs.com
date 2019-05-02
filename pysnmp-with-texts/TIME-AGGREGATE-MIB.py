#
# PySNMP MIB module TIME-AGGREGATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TIME-AGGREGATE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:16:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
OwnerString, = mibBuilder.importSymbols("RMON-MIB", "OwnerString")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
iso, experimental, Integer32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Opaque, Bits, Counter64, Unsigned32, NotificationType, ObjectIdentity, TimeTicks, IpAddress, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "experimental", "Integer32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Opaque", "Bits", "Counter64", "Unsigned32", "NotificationType", "ObjectIdentity", "TimeTicks", "IpAddress", "ModuleIdentity", "Gauge32")
TextualConvention, RowStatus, DisplayString, StorageType = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString", "StorageType")
tAggrMIB = ModuleIdentity((1, 3, 6, 1, 3, 124))
tAggrMIB.setRevisions(('2006-04-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tAggrMIB.setRevisionsDescriptions(('Initial version, published as RFC 4498.',))
if mibBuilder.loadTexts: tAggrMIB.setLastUpdated('200604270000Z')
if mibBuilder.loadTexts: tAggrMIB.setOrganization('Cyber Solutions Inc. NetMan Working Group')
if mibBuilder.loadTexts: tAggrMIB.setContactInfo(' Glenn Mansfield Keeni Postal: Cyber Solutions Inc. 6-6-3, Minami Yoshinari Aoba-ku, Sendai, Japan 989-3204. Tel: +81-22-303-4012 Fax: +81-22-303-4015 E-mail: glenn@cysols.com Support Group E-mail: mibsupport@cysols.com')
if mibBuilder.loadTexts: tAggrMIB.setDescription('The MIB for servicing Time-Based aggregate objects. Copyright (C) The Internet Society (2006). This version of this MIB module is part of RFC 4498; see the RFC itself for full legal notices. ')
class TAggrMOErrorStatus(TextualConvention, Opaque):
    description = 'This data type is used to model the error status of the sampled MO instance. The error status for a sampled MO instance is given in terms of two elements: o The moIndex, which indicates the sample number of the MO instance (starting at 1) in the value of the time- aggregated MO instance. o The moError, which indicates the error that was encountered in sampling that MO instance. The syntax in ASN.1 Notation will be ErrorStatus :: = SEQUENCE { moIndex Integer32, moError SnmpPduErrorStatus } TAggrMOErrorStatus ::= SEQUENCE OF { ErrorStatus } Note1: The command responder will supply values for all the samples of the MO instance. If an error is encountered for a sample, then the corresponding value will have an ASN.1 value NULL, and an error will be flagged in the corresponding TAggrMOErrorStatus object. Only MOs for which errors have been encountered will the corresponding moIndex and moError values be set. Note2: The error code for the component MO instances will be in accordance with the SnmpPduErrorStatus TC defined in the DISMAN-SCHEDULE-MIB[RFC3231]. '
    status = 'current'
    subtypeSpec = Opaque.subtypeSpec + ValueSizeConstraint(0, 1024)

class TimeAggrMOValue(TextualConvention, Opaque):
    description = 'This data type is used to model the time-aggregated MOs. It will be a sequence of values. The syntax in ASN.1 Notation will be MOSampleValue :: = SEQUENCE { value ObjectSyntax } TimeAggrMOValue ::= SEQUENCE OF { MOSampleValue } where the first MOSampleValue, if any, will always be the timestamp of the first sample in the aggregated object. The subsequent values are the values of the MO instance sampled at the specified intervals for the specified number of times. Note: The command generator will need to know the constituent MO instance and the sampling interval to correctly interpret TimeAggrMOValue. '
    status = 'current'
    subtypeSpec = Opaque.subtypeSpec + ValueSizeConstraint(0, 1024)

class CompressedTimeAggrMOValue(TextualConvention, Opaque):
    description = 'This data type is used to model the compressed TAgMOs.'
    status = 'current'
    subtypeSpec = Opaque.subtypeSpec + ValueSizeConstraint(0, 1024)

tAggrCtlTable = MibTable((1, 3, 6, 1, 3, 124, 1), )
if mibBuilder.loadTexts: tAggrCtlTable.setStatus('current')
if mibBuilder.loadTexts: tAggrCtlTable.setDescription('The Time-Based aggregation control table. It controls the aggregation of the samples of MO instances. There will be a row for each TAgMO. ')
tAggrCtlEntry = MibTableRow((1, 3, 6, 1, 3, 124, 1, 1), ).setIndexNames((0, "TIME-AGGREGATE-MIB", "tAggrCtlEntryID"))
if mibBuilder.loadTexts: tAggrCtlEntry.setStatus('current')
if mibBuilder.loadTexts: tAggrCtlEntry.setDescription('A row of the control table that defines one Time-Based aggregate MO (TAgMO).')
tAggrCtlEntryID = MibTableColumn((1, 3, 6, 1, 3, 124, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: tAggrCtlEntryID.setStatus('current')
if mibBuilder.loadTexts: tAggrCtlEntryID.setDescription('A locally unique, administratively assigned name for this aggregated MO. It is used as an index to uniquely identify this row in the table.')
tAggrCtlMOInstance = MibTableColumn((1, 3, 6, 1, 3, 124, 1, 1, 2), ObjectIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tAggrCtlMOInstance.setStatus('current')
if mibBuilder.loadTexts: tAggrCtlMOInstance.setDescription('The sampled values of this MO instance will be aggregated by the TAgMO. ')
tAggrCtlAgMODescr = MibTableColumn((1, 3, 6, 1, 3, 124, 1, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tAggrCtlAgMODescr.setStatus('current')
if mibBuilder.loadTexts: tAggrCtlAgMODescr.setDescription('A textual description of the aggregate object.')
tAggrCtlInterval = MibTableColumn((1, 3, 6, 1, 3, 124, 1, 1, 4), Integer32()).setUnits('micro seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: tAggrCtlInterval.setStatus('current')
if mibBuilder.loadTexts: tAggrCtlInterval.setDescription('The interval, in microseconds, at which the MO instance pointed at by tAggrInstance will be sampled for Time-Based aggregation. ')
tAggrCtlSamples = MibTableColumn((1, 3, 6, 1, 3, 124, 1, 1, 5), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tAggrCtlSamples.setStatus('current')
if mibBuilder.loadTexts: tAggrCtlSamples.setDescription('The number of times at which the MO instance referred to by tAggrInstance will be sampled for Time-Based aggregation.')
tAggrCtlCompressionAlgorithm = MibTableColumn((1, 3, 6, 1, 3, 124, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("deflate", 2))).clone('none')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tAggrCtlCompressionAlgorithm.setReference('RFC1951 : DEFLATE Compressed Data Format Specification version 1.3 ')
if mibBuilder.loadTexts: tAggrCtlCompressionAlgorithm.setStatus('current')
if mibBuilder.loadTexts: tAggrCtlCompressionAlgorithm.setDescription('The compression algorithm that will be used by the agent to compress the value of the TAgMO. The deflate algorithm and corresponding data format specification is described in RFC 1951. It is compatible with the widely used gzip utility. ')
tAggrCtlEntryOwner = MibTableColumn((1, 3, 6, 1, 3, 124, 1, 1, 7), OwnerString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tAggrCtlEntryOwner.setStatus('current')
if mibBuilder.loadTexts: tAggrCtlEntryOwner.setDescription('A textual description of the entity that created this entry. ')
tAggrCtlEntryStorageType = MibTableColumn((1, 3, 6, 1, 3, 124, 1, 1, 8), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tAggrCtlEntryStorageType.setStatus('current')
if mibBuilder.loadTexts: tAggrCtlEntryStorageType.setDescription("This object defines whether the parameters defined in this row are kept in volatile storage and lost upon reboot or backed up by non-volatile (permanent) storage. Conceptual rows having the value 'permanent' need not allow write-access to any columnar objects in the row. ")
tAggrCtlEntryStatus = MibTableColumn((1, 3, 6, 1, 3, 124, 1, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tAggrCtlEntryStatus.setStatus('current')
if mibBuilder.loadTexts: tAggrCtlEntryStatus.setDescription("The row status variable, used according to row installation and removal conventions. Objects in a row can be modified only when the value of this object in the corresponding conceptual row is not 'active'. Thus, to modify one or more of the objects in this conceptual row, a. change the row status to 'notInService', b. change the values of the row, and c. change the row status to 'active'. The tAggrCtlEntryStatus may be changed to 'active' iff all the MOs in the conceptual row have been assigned valid values. ")
tAggrDataTable = MibTable((1, 3, 6, 1, 3, 124, 2), )
if mibBuilder.loadTexts: tAggrDataTable.setStatus('current')
if mibBuilder.loadTexts: tAggrDataTable.setDescription('This is the data table. Each row of this table contains information about a TAgMO indexed by tAggrCtlEntryID. tAggrCtlEntryID is the key to the table. It is used to identify instances of the TAgMO that are present in the table. ')
tAggrDataEntry = MibTableRow((1, 3, 6, 1, 3, 124, 2, 1), ).setIndexNames((0, "TIME-AGGREGATE-MIB", "tAggrCtlEntryID"))
if mibBuilder.loadTexts: tAggrDataEntry.setStatus('current')
if mibBuilder.loadTexts: tAggrDataEntry.setDescription('Entry containing information pertaining to a TAgMO.')
tAggrDataRecord = MibTableColumn((1, 3, 6, 1, 3, 124, 2, 1, 1), TimeAggrMOValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tAggrDataRecord.setStatus('current')
if mibBuilder.loadTexts: tAggrDataRecord.setDescription('The snapshot value of the TAgMO.')
tAggrDataRecordCompressed = MibTableColumn((1, 3, 6, 1, 3, 124, 2, 1, 2), CompressedTimeAggrMOValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tAggrDataRecordCompressed.setStatus('current')
if mibBuilder.loadTexts: tAggrDataRecordCompressed.setDescription("The compressed value of the TAgMO. The compression algorithm will depend on the tAggrCtlCompressionAlgorithm given in the corresponding tAggrCtlEntry. If the value of the corresponding tAggrCtlCompressionAlgorithm is (1) 'none', then the value of all instances of this object will be a string of zero length. Note that the access privileges to this object will be governed by the access privileges of the corresponding MO instance. Thus, an entity attempting to access an instance of this MO MUST have access rights to the instance object pointed at by tAggrCtlMOInstance and this MO instance. ")
tAggrDataErrorRecord = MibTableColumn((1, 3, 6, 1, 3, 124, 2, 1, 3), TAggrMOErrorStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tAggrDataErrorRecord.setStatus('current')
if mibBuilder.loadTexts: tAggrDataErrorRecord.setDescription('The error status corresponding to the MO instance samples aggregated in tAggrDataRecord (and tAggrDataRecordCompressed).')
tAggrConformance = MibIdentifier((1, 3, 6, 1, 3, 124, 3))
tAggrGroups = MibIdentifier((1, 3, 6, 1, 3, 124, 3, 1))
tAggrCompliances = MibIdentifier((1, 3, 6, 1, 3, 124, 3, 2))
tAggrMibCompliance = ModuleCompliance((1, 3, 6, 1, 3, 124, 3, 2, 1)).setObjects(("TIME-AGGREGATE-MIB", "tAggrMibBasicGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tAggrMibCompliance = tAggrMibCompliance.setStatus('current')
if mibBuilder.loadTexts: tAggrMibCompliance.setDescription('The compliance statement for SNMP entities that implement the TIME-AGGREGATE-MIB.')
tAggrMibBasicGroup = ObjectGroup((1, 3, 6, 1, 3, 124, 3, 1, 1)).setObjects(("TIME-AGGREGATE-MIB", "tAggrCtlMOInstance"), ("TIME-AGGREGATE-MIB", "tAggrCtlAgMODescr"), ("TIME-AGGREGATE-MIB", "tAggrCtlInterval"), ("TIME-AGGREGATE-MIB", "tAggrCtlSamples"), ("TIME-AGGREGATE-MIB", "tAggrCtlCompressionAlgorithm"), ("TIME-AGGREGATE-MIB", "tAggrCtlEntryOwner"), ("TIME-AGGREGATE-MIB", "tAggrCtlEntryStorageType"), ("TIME-AGGREGATE-MIB", "tAggrCtlEntryStatus"), ("TIME-AGGREGATE-MIB", "tAggrDataRecord"), ("TIME-AGGREGATE-MIB", "tAggrDataRecordCompressed"), ("TIME-AGGREGATE-MIB", "tAggrDataErrorRecord"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tAggrMibBasicGroup = tAggrMibBasicGroup.setStatus('current')
if mibBuilder.loadTexts: tAggrMibBasicGroup.setDescription('A collection of objects for Time-Based aggregation of MOs.')
mibBuilder.exportSymbols("TIME-AGGREGATE-MIB", tAggrCtlEntryID=tAggrCtlEntryID, tAggrCtlEntryStorageType=tAggrCtlEntryStorageType, tAggrCtlEntryStatus=tAggrCtlEntryStatus, tAggrDataErrorRecord=tAggrDataErrorRecord, tAggrDataRecord=tAggrDataRecord, tAggrGroups=tAggrGroups, tAggrCtlTable=tAggrCtlTable, tAggrCtlEntry=tAggrCtlEntry, TAggrMOErrorStatus=TAggrMOErrorStatus, tAggrMibBasicGroup=tAggrMibBasicGroup, tAggrCompliances=tAggrCompliances, tAggrDataTable=tAggrDataTable, TimeAggrMOValue=TimeAggrMOValue, tAggrCtlSamples=tAggrCtlSamples, CompressedTimeAggrMOValue=CompressedTimeAggrMOValue, tAggrCtlCompressionAlgorithm=tAggrCtlCompressionAlgorithm, tAggrMibCompliance=tAggrMibCompliance, tAggrMIB=tAggrMIB, tAggrDataRecordCompressed=tAggrDataRecordCompressed, tAggrCtlMOInstance=tAggrCtlMOInstance, tAggrCtlAgMODescr=tAggrCtlAgMODescr, PYSNMP_MODULE_ID=tAggrMIB, tAggrConformance=tAggrConformance, tAggrCtlEntryOwner=tAggrCtlEntryOwner, tAggrCtlInterval=tAggrCtlInterval, tAggrDataEntry=tAggrDataEntry)
