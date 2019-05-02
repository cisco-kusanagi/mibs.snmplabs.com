#
# PySNMP MIB module CISCO-VISM-CAS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VISM-CAS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:18:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
voice, = mibBuilder.importSymbols("BASIS-MIB", "voice")
ciscoWan, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWan")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Counter32, Counter64, iso, NotificationType, Gauge32, Bits, ModuleIdentity, Integer32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Counter64", "iso", "NotificationType", "Gauge32", "Bits", "ModuleIdentity", "Integer32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "IpAddress", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoVismCasMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 150, 88))
ciscoVismCasMIB.setRevisions(('2003-07-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVismCasMIB.setRevisionsDescriptions(('Initial version of the MIB. The content of this MIB was originally available in SMIv1 version. The MIB has been converted to SMIv2 version and descriptions of some of the objects have been modified.',))
if mibBuilder.loadTexts: ciscoVismCasMIB.setLastUpdated('200307160000Z')
if mibBuilder.loadTexts: ciscoVismCasMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVismCasMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoVismCasMIB.setDescription('The MIB module contain the CAS backhaul feature in VISM')
vismCasGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 8))
vismCasVariantTable = MibTable((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 8, 1), )
if mibBuilder.loadTexts: vismCasVariantTable.setStatus('current')
if mibBuilder.loadTexts: vismCasVariantTable.setDescription('This table contains configuration information about different CAS variants. ')
vismCasVariantEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 8, 1, 1), ).setIndexNames((0, "CISCO-VISM-CAS-MIB", "vismCasVariantName"))
if mibBuilder.loadTexts: vismCasVariantEntry.setStatus('current')
if mibBuilder.loadTexts: vismCasVariantEntry.setDescription('An entry in the vismCasVariantTable. Each entry consists of configuration information for a specific CAS variant. An entry may be created by specifying vismCasVariantName, and vismCasFileName. Upon the creation of the table entry, the file specified by vismCasFileName will be downloaded and the CAS finite state machine will be initialized based on the information contained in this file. ')
vismCasVariantName = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 8, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismCasVariantName.setStatus('current')
if mibBuilder.loadTexts: vismCasVariantName.setDescription('This object is a string identifier for the CAS variant. It is used as index to the table. The maximum length allowed is 64 bytes. ')
vismCasFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 8, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(2, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismCasFileName.setStatus('current')
if mibBuilder.loadTexts: vismCasFileName.setDescription('This object gives the name of the file which contains the signal definition and the Finite State Machine definition for the CAS variant. The name is supplied during the creation of the table entry. Modifying the value of this object is not allowed. Upon the creation of the table entry, the file will be downloaded from a tftp server configured in the vismTftpServerDn object and the CAS finite state machine will be initialized based on the information contained in this file. This object must be provided in order to create en entry in this table. ')
vismCasTRinging = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 8, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 600)).clone(180)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismCasTRinging.setStatus('deprecated')
if mibBuilder.loadTexts: vismCasTRinging.setDescription(' This object gives the ringing time in seconds for the Cas Variant. The ringing will be on until this timer expires or until an off hook is received. ')
vismCasDigitMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 8, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("mf", 1), ("dtmf", 2))).clone('dtmf')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismCasDigitMethod.setStatus('current')
if mibBuilder.loadTexts: vismCasDigitMethod.setDescription(' The default digit method to be used for digit collection. If the digit method can not be derived from the digit map specified by the call agent in the XGCP message, this digit method will be used. ')
vismCasInterdigitTpart = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 8, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 10000)).clone(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismCasInterdigitTpart.setStatus('current')
if mibBuilder.loadTexts: vismCasInterdigitTpart.setDescription(' This object represents the partial dial timing in seconds and is used along with a digit map as the inter-digit timer. The timer is not started untill the first digit is entered, and the timer is restarted after each new digit is entered untill either a digit map match or mismatch occurs. ')
vismCasInterdigitTcrit = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 8, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000)).clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismCasInterdigitTcrit.setStatus('current')
if mibBuilder.loadTexts: vismCasInterdigitTcrit.setDescription(' This object represents the critical timing in seconds. If used along with a digit map, the timer is started when the last digit is received. i.e and when no more digits are required for a digit map match. After this timer expires, the digit map match is assumed to be complete. If used without a digit map, the timer is started immediately and cancelled (but not restarted) as soon as a digit is entered. ')
vismCasInterdigitTMF = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 8, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismCasInterdigitTMF.setStatus('current')
if mibBuilder.loadTexts: vismCasInterdigitTMF.setDescription('This object represents the interdigit timeout value for MF digits. The timeout value is in seconds. ')
vismCasVariantState = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 8, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notConfigured", 1), ("configInProgress", 2), ("configured", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismCasVariantState.setStatus('current')
if mibBuilder.loadTexts: vismCasVariantState.setDescription('This variable indicates the configuration status of the CAS variant. When the table entry is created, downloading of the file will be initiated and the state will be set to configInProgress. Once the file is successfully downloaded and the CAS finite state machine successfully initialized, the state will be set to configured. If the initialization fails, the state will be set to notConfigured. ')
vismCasRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 8, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 4, 6))).clone(namedValues=NamedValues(("active", 1), ("createAndGo", 4), ("destroy", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismCasRowStatus.setStatus('current')
if mibBuilder.loadTexts: vismCasRowStatus.setDescription('This variable allows to add, delete or modify the entry for a CAS variant. createAndGo: Use this to add an entry in this table, provided the vismCasVariantName and vismCasFileName MIB objects are available to be set. active: This values is returned, once the row is created destroy: Use this to delete an entry from this table. ')
vismCasCountryCode = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 8, 1, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 2)).clone('US')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismCasCountryCode.setStatus('deprecated')
if mibBuilder.loadTexts: vismCasCountryCode.setDescription(' Represents a case-insensitive 2-letter country code taken from ISO-3166. ')
vismCasVariantSource = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 8, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unspecified", 1), ("internal", 2), ("external", 3))).clone('unspecified')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismCasVariantSource.setStatus('current')
if mibBuilder.loadTexts: vismCasVariantSource.setDescription('This object specifies where the file defining this CAS variant resides. 1. Unspecified. This value indicates that the location of the file is not specified here. In this case, the location is determined based on whether the TFTP server domain is defined on VISM. The file is built into the firmware if no tftp domain is defined on VISM and resides on the TFTP server if a TFTP domain is defined on VISM. 2. Internal. Indicates that the file is built into the firmware. 3. External. Indicates that the file resides on the TFTP server configured on VISM. ')
vismCasXgcpVariantTable = MibTable((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 8, 2), )
if mibBuilder.loadTexts: vismCasXgcpVariantTable.setStatus('current')
if mibBuilder.loadTexts: vismCasXgcpVariantTable.setDescription(' An entry in this table is implicitly created/deleted when an entry in vismCasVariantTable is created/deleted in switching mode .')
vismCasXgcpVariantEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 8, 2, 1), ).setIndexNames((0, "CISCO-VISM-CAS-MIB", "vismCasXgcpVariantName"))
if mibBuilder.loadTexts: vismCasXgcpVariantEntry.setStatus('current')
if mibBuilder.loadTexts: vismCasXgcpVariantEntry.setDescription('An entry in the vismCasXgcpVariantTable. ')
vismCasXgcpVariantName = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 8, 2, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismCasXgcpVariantName.setStatus('current')
if mibBuilder.loadTexts: vismCasXgcpVariantName.setDescription(' This object is a string identifier for the CAS variant. It is used as index to the table. ')
vismCasXgcpFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 8, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismCasXgcpFileName.setStatus('current')
if mibBuilder.loadTexts: vismCasXgcpFileName.setDescription(' This object gives the name of the file which contains the signal definition and the Finite State Machine definition for the CAS variant. ')
vismCasXgcpMaxReXmitTime = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 8, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 10000)).clone(500)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismCasXgcpMaxReXmitTime.setStatus('current')
if mibBuilder.loadTexts: vismCasXgcpMaxReXmitTime.setDescription(' This object represents the maximum timeout value in milli seconds, used for retransmitting unacknowledged XGCP messages at the Call Agent - CAS/PBX interface. The value of this object is settable in 10 ms increments. ')
vismCasXgcpInitialReXmitTime = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 8, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 10000)).clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismCasXgcpInitialReXmitTime.setStatus('current')
if mibBuilder.loadTexts: vismCasXgcpInitialReXmitTime.setDescription(' This object represents the initial timeout value in milli seconds, used for retransmitting unacknowledged XGCP messages at the Call Agent - CAS/PBX interface. The value of this object is settable in 10 ms increments. ')
vismCasXgcpMaxRetries = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 8, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10)).clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismCasXgcpMaxRetries.setStatus('current')
if mibBuilder.loadTexts: vismCasXgcpMaxRetries.setDescription(' This object specifies the number of retries for a message that exceeds vismCasXgcpMaxReXmitTime or vismCasXgcpInitialReXmitTime. ')
ciscoVismCasMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 88, 2))
ciscoVismCasMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 88, 2, 1))
ciscoVismCasMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 88, 2, 2))
ciscoVismCasCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 88, 2, 2, 1)).setObjects(("CISCO-VISM-CAS-MIB", "ciscoVismCasVariantGroup"), ("CISCO-VISM-CAS-MIB", "ciscoVismCasXgcpVariantGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVismCasCompliance = ciscoVismCasCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoVismCasCompliance.setDescription('The compliance statement for objects related to VISM-CAS-MIB.')
ciscoVismCasVariantGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 88, 2, 1, 1)).setObjects(("CISCO-VISM-CAS-MIB", "vismCasVariantName"), ("CISCO-VISM-CAS-MIB", "vismCasFileName"), ("CISCO-VISM-CAS-MIB", "vismCasDigitMethod"), ("CISCO-VISM-CAS-MIB", "vismCasInterdigitTpart"), ("CISCO-VISM-CAS-MIB", "vismCasInterdigitTcrit"), ("CISCO-VISM-CAS-MIB", "vismCasInterdigitTMF"), ("CISCO-VISM-CAS-MIB", "vismCasVariantState"), ("CISCO-VISM-CAS-MIB", "vismCasRowStatus"), ("CISCO-VISM-CAS-MIB", "vismCasVariantSource"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVismCasVariantGroup = ciscoVismCasVariantGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoVismCasVariantGroup.setDescription('The collection of objects which are used to represent VISM CAS varient.')
ciscoVismCasXgcpVariantGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 88, 2, 1, 2)).setObjects(("CISCO-VISM-CAS-MIB", "vismCasXgcpVariantName"), ("CISCO-VISM-CAS-MIB", "vismCasXgcpFileName"), ("CISCO-VISM-CAS-MIB", "vismCasXgcpMaxReXmitTime"), ("CISCO-VISM-CAS-MIB", "vismCasXgcpInitialReXmitTime"), ("CISCO-VISM-CAS-MIB", "vismCasXgcpMaxRetries"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVismCasXgcpVariantGroup = ciscoVismCasXgcpVariantGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoVismCasXgcpVariantGroup.setDescription('The collection of objects that is implicitly created/deleted when an entry in vismCasVariantTable is created/deleted in switching mode.')
cvcVariantDeprecatedGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 88, 2, 1, 3)).setObjects(("CISCO-VISM-CAS-MIB", "vismCasTRinging"), ("CISCO-VISM-CAS-MIB", "vismCasCountryCode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvcVariantDeprecatedGroup = cvcVariantDeprecatedGroup.setStatus('deprecated')
if mibBuilder.loadTexts: cvcVariantDeprecatedGroup.setDescription('The collection of objects that were supported earlier but deprecated now.')
mibBuilder.exportSymbols("CISCO-VISM-CAS-MIB", ciscoVismCasMIB=ciscoVismCasMIB, vismCasVariantName=vismCasVariantName, ciscoVismCasMIBGroups=ciscoVismCasMIBGroups, vismCasFileName=vismCasFileName, vismCasRowStatus=vismCasRowStatus, vismCasXgcpMaxRetries=vismCasXgcpMaxRetries, vismCasVariantState=vismCasVariantState, vismCasGrp=vismCasGrp, PYSNMP_MODULE_ID=ciscoVismCasMIB, vismCasVariantSource=vismCasVariantSource, vismCasXgcpVariantName=vismCasXgcpVariantName, ciscoVismCasMIBConformance=ciscoVismCasMIBConformance, ciscoVismCasMIBCompliances=ciscoVismCasMIBCompliances, vismCasXgcpFileName=vismCasXgcpFileName, vismCasXgcpInitialReXmitTime=vismCasXgcpInitialReXmitTime, vismCasInterdigitTpart=vismCasInterdigitTpart, vismCasVariantTable=vismCasVariantTable, vismCasXgcpVariantTable=vismCasXgcpVariantTable, vismCasXgcpMaxReXmitTime=vismCasXgcpMaxReXmitTime, cvcVariantDeprecatedGroup=cvcVariantDeprecatedGroup, vismCasInterdigitTcrit=vismCasInterdigitTcrit, ciscoVismCasXgcpVariantGroup=ciscoVismCasXgcpVariantGroup, vismCasInterdigitTMF=vismCasInterdigitTMF, vismCasXgcpVariantEntry=vismCasXgcpVariantEntry, ciscoVismCasVariantGroup=ciscoVismCasVariantGroup, vismCasTRinging=vismCasTRinging, vismCasDigitMethod=vismCasDigitMethod, ciscoVismCasCompliance=ciscoVismCasCompliance, vismCasCountryCode=vismCasCountryCode, vismCasVariantEntry=vismCasVariantEntry)
