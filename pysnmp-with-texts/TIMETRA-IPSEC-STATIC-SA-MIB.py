#
# PySNMP MIB module TIMETRA-IPSEC-STATIC-SA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TIMETRA-IPSEC-STATIC-SA-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:18:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
NotificationType, Counter32, Bits, ObjectIdentity, Unsigned32, MibIdentifier, Gauge32, IpAddress, Counter64, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter32", "Bits", "ObjectIdentity", "Unsigned32", "MibIdentifier", "Gauge32", "IpAddress", "Counter64", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Integer32", "iso")
DisplayString, TimeStamp, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TimeStamp", "RowStatus", "TextualConvention")
tmnxSRObjs, timetraSRMIBModules, tmnxSRConfs = mibBuilder.importSymbols("TIMETRA-GLOBAL-MIB", "tmnxSRObjs", "timetraSRMIBModules", "tmnxSRConfs")
TNamedItemOrEmpty, TNamedItem = mibBuilder.importSymbols("TIMETRA-TC-MIB", "TNamedItemOrEmpty", "TNamedItem")
timetraIPsecStaticSAMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 73))
timetraIPsecStaticSAMIBModule.setRevisions(('1909-12-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: timetraIPsecStaticSAMIBModule.setRevisionsDescriptions(('Rev 8.0 14 Dec 2009 00:00 8.0 release of the TIMETRA-IPSEC-STATIC-SA-MIB.',))
if mibBuilder.loadTexts: timetraIPsecStaticSAMIBModule.setLastUpdated('0912140000Z')
if mibBuilder.loadTexts: timetraIPsecStaticSAMIBModule.setOrganization('Alcatel-Lucent')
if mibBuilder.loadTexts: timetraIPsecStaticSAMIBModule.setContactInfo('Alcatel-Lucent SROS Support Web: http://support.alcatel-lucent.com')
if mibBuilder.loadTexts: timetraIPsecStaticSAMIBModule.setDescription("This document is the SNMP MIB module to manage and provision the Alcatel-Lucent SROS device with IPsec Static SA tunneling, encryption and other related features. Copyright 2008-2011 Alcatel-Lucent. All rights reserved. Reproduction of this document is authorized on the condition that the foregoing copyright notice is included. This SNMP MIB module (Specification) embodies Alcatel-Lucent's proprietary intellectual property. Alcatel-Lucent retains all title and ownership in the Specification, including any revisions. Alcatel-Lucent grants all interested parties a non-exclusive license to use and distribute an unmodified copy of this Specification in connection with management of Alcatel-Lucent products, and without fee, provided this copyright notice and license appear on all copies. This Specification is supplied 'as is', and Alcatel-Lucent makes no warranty, either express or implied, as to the use, operation, condition, or performance of the Specification.")
tmnxIPsecStaticSAObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 73))
tmnxIPsecStaticSAConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 73))
class TmnxAuthAlgorithm(TextualConvention, Integer32):
    description = 'TmnxAuthAlgorithm data type is an enumerated integer that describes the values used to identify the hashing algorithm. Value Descriptions: null - Choosing this value configures the high-speed null algorithm, which does nothing. This is same as not having authentication turned on, same as turning the protocol off. md5 - Choosing this value configures the use of hmac-md5 algorithm for authentication. sha1 - Choosing this valule configures the use of hmac-sha1 algorithm for authentication.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("null", 1), ("md5", 2), ("sha1", 3))

class TmnxIPsecDirection2(TextualConvention, Integer32):
    description = 'TmnxIPsecDirection data type is an enumerated integer that describes the values used to identify the direction of an IPsec tunnel.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("inbound", 1), ("outbound", 2), ("bidirectional", 3))

class TmnxIPsecProtocol(TextualConvention, Integer32):
    description = 'TmnxIPsecProtocol data type is an enumerated integer that describes the values used to identify the used IPsec protocol.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ah", 1), ("esp", 2))

tmnxIPsecStaticSATableLastChange = MibScalar((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 73, 1), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmnxIPsecStaticSATableLastChange.setStatus('current')
if mibBuilder.loadTexts: tmnxIPsecStaticSATableLastChange.setDescription('The value of tmnxIPsecStaticSATableLastChange indicates the sysUpTime at the time of the last modification to tmnxIPsecStaticSATable by adding, deleting an entry or change to a writable object in the table. If no changes were made to the table since the last re-initialization of the local network management subsystem, then this object contains a zero value.')
tmnxIPsecStaticSATable = MibTable((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 73, 2), )
if mibBuilder.loadTexts: tmnxIPsecStaticSATable.setStatus('current')
if mibBuilder.loadTexts: tmnxIPsecStaticSATable.setDescription('Table to store the IPsec static SA entries.')
tmnxIPsecStaticSAEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 73, 2, 1), ).setIndexNames((1, "TIMETRA-IPSEC-STATIC-SA-MIB", "tmnxIPsecStaticSAName"))
if mibBuilder.loadTexts: tmnxIPsecStaticSAEntry.setStatus('current')
if mibBuilder.loadTexts: tmnxIPsecStaticSAEntry.setDescription('Information about a single IPsec static SA entry.')
tmnxIPsecStaticSAName = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 73, 2, 1, 1), TNamedItem())
if mibBuilder.loadTexts: tmnxIPsecStaticSAName.setStatus('current')
if mibBuilder.loadTexts: tmnxIPsecStaticSAName.setDescription('The value of tmnxIPsecStaticSAName specifies the name of this static SA and is part of the index for the table tmnxIPsecStaticSATable, and thus a required object.')
tmnxIPsecStaticSARowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 73, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tmnxIPsecStaticSARowStatus.setStatus('current')
if mibBuilder.loadTexts: tmnxIPsecStaticSARowStatus.setDescription("The tmnxIPsecStaticSARowStatus object is used to create and delete rows in the tmnxIPsecStaticSATable. When creating an entry in tmnxIPsecStaticSATable, the value of tmnxIPsecStaticSARowStatus must be 'createAndGo'.")
tmnxIPsecStaticSALastChanged = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 73, 2, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmnxIPsecStaticSALastChanged.setStatus('current')
if mibBuilder.loadTexts: tmnxIPsecStaticSALastChanged.setDescription('The value of tmnxIPsecStaticSALastChanged indicates the sysUpTime at the time of the last modification of this entry. If no changes were made to the entry since the last re-initialization of the local network management subsystem, then this object contains a zero value.')
tmnxIPsecStaticSADirection = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 73, 2, 1, 4), TmnxIPsecDirection2().clone('bidirectional')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tmnxIPsecStaticSADirection.setStatus('current')
if mibBuilder.loadTexts: tmnxIPsecStaticSADirection.setDescription('The value of tmnxIPsecStaticSADirection specifies the direction to which this static SA entry can be applied. This is an optional object when creating an entry in tmnxIPsecStaticSATable.')
tmnxIPsecStaticSAProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 73, 2, 1, 5), TmnxIPsecProtocol().clone('esp')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tmnxIPsecStaticSAProtocol.setStatus('current')
if mibBuilder.loadTexts: tmnxIPsecStaticSAProtocol.setDescription('The value of tmnxIPsecStaticSAProtocol specifies the protocol used by this static SA. This is an optional object when creating an entry in tmnxIPsecStaticSATable.')
tmnxIPsecStaticSAAuthAlgorithm = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 73, 2, 1, 6), TmnxAuthAlgorithm().clone('sha1')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tmnxIPsecStaticSAAuthAlgorithm.setStatus('current')
if mibBuilder.loadTexts: tmnxIPsecStaticSAAuthAlgorithm.setDescription("The value of tmnxIPsecStaticSAAuthAlgorithm indicates the authentication algorithm used with this static SA. The 'md5' algorithm requires a 16 byte key, and the 'sha1' algorithm requires a 20 byte key. This is an optional object when creating an entry in tmnxIPsecStaticSATable.")
tmnxIPsecStaticSAAuthKey = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 73, 2, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tmnxIPsecStaticSAAuthKey.setStatus('current')
if mibBuilder.loadTexts: tmnxIPsecStaticSAAuthKey.setDescription("The value of tmnxIPsecStaticSAAuthKey specifies the key used for the authentication algorithm defined by tmnxIPsecStaticSAAuthAlgorithm. The length of the key must match the length required by the authentication algorithm. If a key of another length is set, the request will fail with an 'inconsistentValue' error. The default value for tmnxIPsecStaticSAAuthKey is an empty string, in this case the static SA cannot be used. When read, tmnxIPsecStaticSAAuthKey always returns an octet string of length zero. This is an optional object when creating an entry in tmnxIPsecStaticSATable.")
tmnxIPsecStaticSASpi = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 73, 2, 1, 8), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(256, 16383), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tmnxIPsecStaticSASpi.setStatus('current')
if mibBuilder.loadTexts: tmnxIPsecStaticSASpi.setDescription("The value of tmnxIPsecStaticSASpi specifies the SPI (Security Parameter Index) used to lookup the instruction to verify and decrypt the incoming IPsec packets when the value of tmnxIPsecStaticSADirection is 'inbound'. The value of tmnxIPsecStaticSASpi specifies the SPI that will be used in the encoding of the outgoing packets when the value of tmnxIPsecStaticSADirection is 'outbound'. The remote node can use this SPI to lookup the instruction to verify and decrypt the packet. If 'no' SPI is selected, then this static SA cannot be used. This is an optional object when creating an entry in tmnxIPsecStaticSATable.")
tmnxIPsecStaticSADescription = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 73, 2, 1, 9), TNamedItemOrEmpty()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tmnxIPsecStaticSADescription.setStatus('current')
if mibBuilder.loadTexts: tmnxIPsecStaticSADescription.setDescription('The value of tmnxIPsecStaticSADescription describes this static SA. This is an optional object when creating an entry in tmnxIPsecStaticSATable.')
tmnxIPsecStaticSACompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 73, 1))
tmnxIPsecStaticSAGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 73, 2))
tmnxIPsecStaticSAV8v0Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 73, 1, 1)).setObjects(("TIMETRA-IPSEC-STATIC-SA-MIB", "tmnxIPsecStaticSAGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmnxIPsecStaticSAV8v0Compliance = tmnxIPsecStaticSAV8v0Compliance.setStatus('current')
if mibBuilder.loadTexts: tmnxIPsecStaticSAV8v0Compliance.setDescription('The compliance statement for management of IPsec static SA features on Alcatel 7x50 SR series systems.')
tmnxIPsecStaticSAGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 73, 2, 1)).setObjects(("TIMETRA-IPSEC-STATIC-SA-MIB", "tmnxIPsecStaticSATableLastChange"), ("TIMETRA-IPSEC-STATIC-SA-MIB", "tmnxIPsecStaticSARowStatus"), ("TIMETRA-IPSEC-STATIC-SA-MIB", "tmnxIPsecStaticSALastChanged"), ("TIMETRA-IPSEC-STATIC-SA-MIB", "tmnxIPsecStaticSADirection"), ("TIMETRA-IPSEC-STATIC-SA-MIB", "tmnxIPsecStaticSAProtocol"), ("TIMETRA-IPSEC-STATIC-SA-MIB", "tmnxIPsecStaticSAAuthAlgorithm"), ("TIMETRA-IPSEC-STATIC-SA-MIB", "tmnxIPsecStaticSAAuthKey"), ("TIMETRA-IPSEC-STATIC-SA-MIB", "tmnxIPsecStaticSASpi"), ("TIMETRA-IPSEC-STATIC-SA-MIB", "tmnxIPsecStaticSADescription"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmnxIPsecStaticSAGroup = tmnxIPsecStaticSAGroup.setStatus('current')
if mibBuilder.loadTexts: tmnxIPsecStaticSAGroup.setDescription('The group of objects for IPsec static SA on Alcatel 7xx0 SR series systems.')
mibBuilder.exportSymbols("TIMETRA-IPSEC-STATIC-SA-MIB", tmnxIPsecStaticSAProtocol=tmnxIPsecStaticSAProtocol, tmnxIPsecStaticSAConformance=tmnxIPsecStaticSAConformance, tmnxIPsecStaticSAAuthAlgorithm=tmnxIPsecStaticSAAuthAlgorithm, tmnxIPsecStaticSADescription=tmnxIPsecStaticSADescription, tmnxIPsecStaticSACompliances=tmnxIPsecStaticSACompliances, tmnxIPsecStaticSATableLastChange=tmnxIPsecStaticSATableLastChange, tmnxIPsecStaticSAV8v0Compliance=tmnxIPsecStaticSAV8v0Compliance, tmnxIPsecStaticSATable=tmnxIPsecStaticSATable, tmnxIPsecStaticSAGroups=tmnxIPsecStaticSAGroups, tmnxIPsecStaticSAAuthKey=tmnxIPsecStaticSAAuthKey, tmnxIPsecStaticSAObjects=tmnxIPsecStaticSAObjects, TmnxIPsecDirection2=TmnxIPsecDirection2, tmnxIPsecStaticSASpi=tmnxIPsecStaticSASpi, TmnxIPsecProtocol=TmnxIPsecProtocol, tmnxIPsecStaticSAGroup=tmnxIPsecStaticSAGroup, TmnxAuthAlgorithm=TmnxAuthAlgorithm, tmnxIPsecStaticSAEntry=tmnxIPsecStaticSAEntry, tmnxIPsecStaticSARowStatus=tmnxIPsecStaticSARowStatus, timetraIPsecStaticSAMIBModule=timetraIPsecStaticSAMIBModule, tmnxIPsecStaticSAName=tmnxIPsecStaticSAName, tmnxIPsecStaticSALastChanged=tmnxIPsecStaticSALastChanged, tmnxIPsecStaticSADirection=tmnxIPsecStaticSADirection, PYSNMP_MODULE_ID=timetraIPsecStaticSAMIBModule)
