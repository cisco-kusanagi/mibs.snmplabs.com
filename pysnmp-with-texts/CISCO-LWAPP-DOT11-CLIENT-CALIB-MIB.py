#
# PySNMP MIB module CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:05:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
cLApSysMacAddress, cLApDot11IfSlotId = mibBuilder.importSymbols("CISCO-LWAPP-AP-MIB", "cLApSysMacAddress", "cLApDot11IfSlotId")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Gauge32, ObjectIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, iso, IpAddress, Counter64, ModuleIdentity, Unsigned32, NotificationType, MibIdentifier, Counter32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ObjectIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "iso", "IpAddress", "Counter64", "ModuleIdentity", "Unsigned32", "NotificationType", "MibIdentifier", "Counter32", "Integer32")
MacAddress, TextualConvention, TruthValue, DisplayString, StorageType, RowStatus, TimeInterval, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "TruthValue", "DisplayString", "StorageType", "RowStatus", "TimeInterval", "TimeStamp")
ciscoLwappDot11ClientCalibMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 522))
ciscoLwappDot11ClientCalibMIB.setRevisions(('2011-11-25 00:00', '2007-02-12 00:00', '2006-04-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoLwappDot11ClientCalibMIB.setRevisionsDescriptions(('Added following OBJECT-GROUP: - cLD11ClientCalibClientConfigGroup - cLD11ClientCalibGlobalConfigGroup - cLD11ClientCalibRssiDataSampleGroup Depreated following OBJECT-GROUP: - ciscoLwappDot11ClientCalibMIBConfigGroup Added new compliance: - ciscoLwappDot11ClientCalibMIBComplianceRev1', 'Added ciscoLwappDot11ClientCalibMIBConfigGroupSup1 OBJECT-GROUP.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoLwappDot11ClientCalibMIB.setLastUpdated('201111250000Z')
if mibBuilder.loadTexts: ciscoLwappDot11ClientCalibMIB.setOrganization('Cisco Systems Inc.')
if mibBuilder.loadTexts: ciscoLwappDot11ClientCalibMIB.setContactInfo('Cisco Systems, Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS Email: cs-wnbu-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoLwappDot11ClientCalibMIB.setDescription('This MIB is intended to be implemented on all those devices operating as Central controllers, that terminate the Light Weight Access Point Protocol tunnel from Cisco Light-weight LWAPP Access Points. Information provided by this MIB is about the configuration and monitoring of 802.11 wireless clients in the network. The relationship between CC and the LWAPP APs can be depicted as follows: +......+ +......+ +......+ +......+ + + + + + + + + + CC + + CC + + CC + + CC + + + + + + + + + +......+ +......+ +......+ +......+ .. . . . .. . . . . . . . . . . . . . . . . . . . . . . . +......+ +......+ +......+ +......+ +......+ + + + + + + + + + + + AP + + AP + + AP + + AP + + AP + + + + + + + + + + + +......+ +......+ +......+ +......+ +......+ . . . . . . . . . . . . . . . . . . . . . . . . +......+ +......+ +......+ +......+ +......+ + + + + + + + + + + + MN + + MN + + MN + + MN + + MN + + + + + + + + + + + +......+ +......+ +......+ +......+ +......+ The LWAPP tunnel exists between the controller and the APs. The MNs communicate with the APs through the protocol defined by the 802.11 standard. LWAPP APs, upon bootup, discover and join one of the controllers and the controller pushes the configuration, that includes the WLAN parameters, to the LWAPP APs. The APs then encapsulate all the 802.11 frames from wireless clients inside LWAPP frames and forward the LWAPP frames to the controller. GLOSSARY Access Point ( AP ) ------------------- An entity that contains an 802.11 medium access control ( MAC ) and physical layer ( PHY ) interface and provides access to the distribution services via the wireless medium for associated clients. LWAPP APs encapsulate all the 802.11 frames in LWAPP frames and sends them to the controller to which it is logically connected. Light Weight Access Point Protocol ( LWAPP ) -------------------------------------------- This is a generic protocol that defines the communication between the Access Points and the Central Controller. Mobile Node ( MN ) ------------------ A roaming 802.11 wireless device in a wireless network associated with an access point. Mobile Node, Mobile Station(Ms) and client are used interchangeably. Signal to Noise Ratio ( SNR ) ----------------------------- It is a measure used in science and engineering that compares the level of a desired signal to the level of background noise. It is defined as the ratio of signal power to the noise power. A ratio higher than 1:1 indicates more signal than noise. While SNR is commonly quoted for electrical signals, it can be applied to any form of signal. Received Signal Strength Indicator ( RSSI ) ------------------------------------------- It is a measurement of the power present in a received radio signal. Radio Frequency Identification ( RFID ) ------------------------------------------- It is a technology that uses radio waves to transfer data from an electronic tag, called RFID tag or label, attached to an object, through a reader for the purpose of identifying and tracking the object. REFERENCE [1] Wireless LAN Medium Access Control ( MAC ) and Physical Layer ( PHY ) Specifications [2] Draft-obara-capwap-lwapp-00.txt, IETF Light Weight Access Point Protocol')
ciscoLwappDot11ClientCalibMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 522, 0))
ciscoLwappDot11ClientCalibMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 522, 1))
ciscoLwappDot11ClientCalibMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 522, 2))
cldccConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1))
cldccStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 2))
cldccRssiSamples = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 2, 1))
cLD11ClientCalibTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1, 1), )
if mibBuilder.loadTexts: cLD11ClientCalibTable.setStatus('current')
if mibBuilder.loadTexts: cLD11ClientCalibTable.setDescription("This table represents the calibration for the 802.11 wireless clients that would associate to the APs that have joined this controller. An entry is created through an explicit management action initiated by the administrator through a network management station by specifying the calibration parameters for a particular client identified by cLD11ClientCalibMacAddress and setting the RowStatus object to 'createAndGo'. An existing entry is deleted by setting the RowStatus object to 'destroy'. The object cLD11ClientCalibTableMaxEntries represents the maximum number of entries in this table.")
cLD11ClientCalibEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibMacAddress"))
if mibBuilder.loadTexts: cLD11ClientCalibEntry.setStatus('current')
if mibBuilder.loadTexts: cLD11ClientCalibEntry.setDescription('Each entry represents a conceptual row in this table and provides the information about the calibration parameters for wireless clients.')
cLD11ClientCalibMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1, 1, 1, 1), MacAddress())
if mibBuilder.loadTexts: cLD11ClientCalibMacAddress.setStatus('current')
if mibBuilder.loadTexts: cLD11ClientCalibMacAddress.setDescription('This object specifies the MAC address of the 802.11 wireless client for which the calibration parameters in this entry are applicable and uniquely identifies this entry.')
cLD11ClientCalibBeaconInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1, 1, 1, 2), TimeInterval().subtype(subtypeSpec=ValueRangeConstraint(400, 3240000)).clone(60000)).setUnits('hundredths-seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cLD11ClientCalibBeaconInterval.setStatus('deprecated')
if mibBuilder.loadTexts: cLD11ClientCalibBeaconInterval.setDescription("This object specifies the time interval, expressed here in hundredths of a second at which an AP issues radio measurement request messages to a client for every SSID. It is not recommended to configure values less than 10 seconds (1000). The value configured through this object is reflected in the operation of the LWAPP APs only if cLD11ClientCalibBeaconEnabled is set to 'true'. This object has been deprecated and is replaced by the object cLD11ClientCalibBeaconIntervalExt.")
cLD11ClientCalibRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cLD11ClientCalibRowStatus.setStatus('current')
if mibBuilder.loadTexts: cLD11ClientCalibRowStatus.setDescription("The object that represents the status of a specific instance of a row in this table. Initially set to a value of 'createAndGo' by the User when a row is created, the status as represented by this object is automatically set to 'active' if and when the row creation is successful. To delete the specific instance of a row, User should set this object to 'destroy'. To create an entry in this table, it is mandatory to specify the cLD11ClientCalibMacAddress, cLD11ClientCalibNumberOfRadios (number of radios to be used in the calibration) and cLD11ClientCalibNumberOfSamples (no. of calibration samples to be collected per radio).")
cLD11ClientCalibNumberOfRadios = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1, 1, 1, 4), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cLD11ClientCalibNumberOfRadios.setStatus('current')
if mibBuilder.loadTexts: cLD11ClientCalibNumberOfRadios.setDescription('This object specifies the number of radios used in this calibration.')
cLD11ClientCalibNumberOfSamples = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cLD11ClientCalibNumberOfSamples.setStatus('current')
if mibBuilder.loadTexts: cLD11ClientCalibNumberOfSamples.setDescription('This object specifies the number of RSSI samples for a given radio, used in this calibration.')
cLD11ClientCalibSamplesCollected = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLD11ClientCalibSamplesCollected.setStatus('current')
if mibBuilder.loadTexts: cLD11ClientCalibSamplesCollected.setDescription('This object indicates the number of samples available for this client.')
cLD11ClientCalibBeaconIntervalExt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1, 1, 1, 7), TimeInterval().clone(60000)).setUnits('hundredths-seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cLD11ClientCalibBeaconIntervalExt.setStatus('current')
if mibBuilder.loadTexts: cLD11ClientCalibBeaconIntervalExt.setDescription("This object specifies the time interval, expressed here in hundredths of a second at which an AP issues radio measurement request messages to a client for every SSID. It is not recommended to configure values less than 10 seconds (1000). The value configured through this object is reflected in the operation of the LWAPP APs only if cLD11ClientCalibBeaconEnabled is set to 'true'.")
cLD11ClientCalibStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1, 1, 1, 8), StorageType().clone('volatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cLD11ClientCalibStorageType.setStatus('current')
if mibBuilder.loadTexts: cLD11ClientCalibStorageType.setDescription('This object specifies the storage type of this conceptual row.')
cLD11ClientCalibTableMaxEntries = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 25))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLD11ClientCalibTableMaxEntries.setStatus('current')
if mibBuilder.loadTexts: cLD11ClientCalibTableMaxEntries.setDescription('This object specifies the maximum number of entries allowed in cLD11ClientCalibTable.')
cLD11ClientCalibDataTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 2, 1, 1), )
if mibBuilder.loadTexts: cLD11ClientCalibDataTable.setStatus('current')
if mibBuilder.loadTexts: cLD11ClientCalibDataTable.setDescription('This table contains the RSSI data samples collected for 802.11 client based on the information provided in the cldccLD11ClientCalibTable. Entries are automatically added by the controller as and when samples are available. This data is used by the NMS for location calibration of the 8022.11 clients.')
cLD11ClientCalibDataEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 2, 1, 1, 1), ).setIndexNames((0, "CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibMacAddress"), (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"), (0, "CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"), (0, "CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "clD11ClientCalibDataTimeStamp"), (0, "CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "clD11ClientCalibDataAntennaIndex"))
if mibBuilder.loadTexts: cLD11ClientCalibDataEntry.setStatus('current')
if mibBuilder.loadTexts: cLD11ClientCalibDataEntry.setDescription('Each entry represents a conceptual row in this table and provides the information about the samples for location calibration of a 802.11 client.')
clD11ClientCalibDataTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 2, 1, 1, 1, 1), TimeStamp()).setUnits('milliseconds')
if mibBuilder.loadTexts: clD11ClientCalibDataTimeStamp.setStatus('current')
if mibBuilder.loadTexts: clD11ClientCalibDataTimeStamp.setDescription('This object indicates the time this sample was collected. This is the absolute system time that this sample was collected.')
clD11ClientCalibDataAntennaIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 2, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("antenna1", 1), ("antenna2", 2))))
if mibBuilder.loadTexts: clD11ClientCalibDataAntennaIndex.setStatus('current')
if mibBuilder.loadTexts: clD11ClientCalibDataAntennaIndex.setDescription('This object indicates the antenna which received the probe request from client.')
clD11ClientCalibDataRssiValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 2, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clD11ClientCalibDataRssiValue.setStatus('current')
if mibBuilder.loadTexts: clD11ClientCalibDataRssiValue.setDescription('This object indicates the RSSI value for this sample.')
clD11ClientCalibDataTransmitPower = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 2, 1, 1, 1, 4), Integer32()).setUnits('dbm').setMaxAccess("readonly")
if mibBuilder.loadTexts: clD11ClientCalibDataTransmitPower.setStatus('current')
if mibBuilder.loadTexts: clD11ClientCalibDataTransmitPower.setDescription('This object indicates the transmit power level for a calibrating client.')
cLD11ClientCalibRssiAlgorithm = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("simple", 2), ("average", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLD11ClientCalibRssiAlgorithm.setStatus('current')
if mibBuilder.loadTexts: cLD11ClientCalibRssiAlgorithm.setDescription('This object specifies the algorithm used to average RSSI and SNR values. unknown(1) - the algorithm used is unknown simple(2) - simple is used for the calculation average(3) - average RSSI is used as algorithm')
cLD11ClientCalibRssiClientExpiryTimeout = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1, 4), Unsigned32()).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLD11ClientCalibRssiClientExpiryTimeout.setStatus('current')
if mibBuilder.loadTexts: cLD11ClientCalibRssiClientExpiryTimeout.setDescription('This object specifies the expiry timeout for the client.')
cLD11ClientCalibRssiCalibClientExpiryTimeout = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1, 5), Unsigned32()).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLD11ClientCalibRssiCalibClientExpiryTimeout.setStatus('current')
if mibBuilder.loadTexts: cLD11ClientCalibRssiCalibClientExpiryTimeout.setDescription('This object specifies the expiry timeout for the calibrating client.')
cLD11ClientCalibRssiRfidTagExpiryTimeout = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1, 6), Unsigned32()).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLD11ClientCalibRssiRfidTagExpiryTimeout.setStatus('current')
if mibBuilder.loadTexts: cLD11ClientCalibRssiRfidTagExpiryTimeout.setDescription('This object specifies the expiry timeout for the RFID tags.')
cLD11ClientCalibRssiRogueApExpiryTimeout = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1, 7), Unsigned32()).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLD11ClientCalibRssiRogueApExpiryTimeout.setStatus('current')
if mibBuilder.loadTexts: cLD11ClientCalibRssiRogueApExpiryTimeout.setDescription('This object specifies the expiry timeout for the Rogue APs.')
cLD11ClientCalibRssiClientHalflifeTimeout = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1, 8), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 2), ValueRangeConstraint(5, 5), ValueRangeConstraint(10, 10), ValueRangeConstraint(20, 20), ValueRangeConstraint(30, 30), ValueRangeConstraint(60, 60), ValueRangeConstraint(90, 90), ValueRangeConstraint(120, 120), ValueRangeConstraint(180, 180), ValueRangeConstraint(300, 300), ))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLD11ClientCalibRssiClientHalflifeTimeout.setStatus('current')
if mibBuilder.loadTexts: cLD11ClientCalibRssiClientHalflifeTimeout.setDescription('This object specifies the half-life timeout for the client. A value of 0 indicates that timeout is disabled.')
cLD11ClientCalibRssiCalibClientHalflifeTimeout = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1, 9), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 2), ValueRangeConstraint(5, 5), ValueRangeConstraint(10, 10), ValueRangeConstraint(20, 20), ValueRangeConstraint(30, 30), ValueRangeConstraint(60, 60), ValueRangeConstraint(90, 90), ValueRangeConstraint(120, 120), ValueRangeConstraint(180, 180), ValueRangeConstraint(300, 300), ))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLD11ClientCalibRssiCalibClientHalflifeTimeout.setStatus('current')
if mibBuilder.loadTexts: cLD11ClientCalibRssiCalibClientHalflifeTimeout.setDescription('This object specifies the half-life timeout for the calibrating client. A value of 0 indicates that timeout is disabled.')
cLD11ClientCalibRssiRfidTagHalflifeTimeout = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1, 10), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 2), ValueRangeConstraint(5, 5), ValueRangeConstraint(10, 10), ValueRangeConstraint(20, 20), ValueRangeConstraint(30, 30), ValueRangeConstraint(60, 60), ValueRangeConstraint(90, 90), ValueRangeConstraint(120, 120), ValueRangeConstraint(180, 180), ValueRangeConstraint(300, 300), ))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLD11ClientCalibRssiRfidTagHalflifeTimeout.setStatus('current')
if mibBuilder.loadTexts: cLD11ClientCalibRssiRfidTagHalflifeTimeout.setDescription('This object specifies the half-life timeout for the RFID tags. A value of 0 indicates that timeout is disabled.')
cLD11ClientCalibRssiRogueApHalflifeTimeout = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1, 11), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 2), ValueRangeConstraint(5, 5), ValueRangeConstraint(10, 10), ValueRangeConstraint(20, 20), ValueRangeConstraint(30, 30), ValueRangeConstraint(60, 60), ValueRangeConstraint(90, 90), ValueRangeConstraint(120, 120), ValueRangeConstraint(180, 180), ValueRangeConstraint(300, 300), ))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLD11ClientCalibRssiRogueApHalflifeTimeout.setStatus('current')
if mibBuilder.loadTexts: cLD11ClientCalibRssiRogueApHalflifeTimeout.setDescription('This object specifies the half-life timeout for the Rogue APs. A value of 0 indicates that timeout is disabled.')
cLD11ClientCalibRfidDataEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1, 12), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLD11ClientCalibRfidDataEnable.setStatus('current')
if mibBuilder.loadTexts: cLD11ClientCalibRfidDataEnable.setDescription('This object specifies whether the RFID tag data collection is enabled.')
cLD11ClientCalibRfidTimeout = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1, 13), Unsigned32()).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLD11ClientCalibRfidTimeout.setStatus('current')
if mibBuilder.loadTexts: cLD11ClientCalibRfidTimeout.setDescription('This object specifies the RFID tag data timeout.')
cLD11ClientCalibClientMultiBandEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1, 14), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLD11ClientCalibClientMultiBandEnable.setStatus('current')
if mibBuilder.loadTexts: cLD11ClientCalibClientMultiBandEnable.setDescription('This object specifies whether calibrating client uses both the bands to transmit the requests. true - the calibrating client uses both the bands to transmit the requests. false - the calibrating client uses single band to transmit the requests.')
cLD11ClientCalibClientRequestEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1, 15), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLD11ClientCalibClientRequestEnable.setStatus('current')
if mibBuilder.loadTexts: cLD11ClientCalibClientRequestEnable.setDescription('This object specifies whether calibrating client uses uni band or multi band to transmit the requests. true - the calibrating client uses uni band or multi band to transmit the requests. false - the calibrating client does not use any band for transmitting requests.')
cLD11ClientCalibClientBurstIntervalEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1, 16), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLD11ClientCalibClientBurstIntervalEnable.setStatus('current')
if mibBuilder.loadTexts: cLD11ClientCalibClientBurstIntervalEnable.setDescription('This object specifies whether calibrating client burst interval is enabled. true - the calibrating client burst interval is enabled. false - the calibrating client burst interval is disabled.')
cLD11ClientCalibClientBurstInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1, 17), Unsigned32()).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLD11ClientCalibClientBurstInterval.setStatus('current')
if mibBuilder.loadTexts: cLD11ClientCalibClientBurstInterval.setDescription('This object specifies the burst interval of the calibrating client.')
cLD11ClientCalibClientInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1, 18), Unsigned32()).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLD11ClientCalibClientInterval.setStatus('current')
if mibBuilder.loadTexts: cLD11ClientCalibClientInterval.setDescription('This object specifies the notification interval for calibrating clients.')
cLD11ClientCalibRfidInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1, 19), Unsigned32()).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLD11ClientCalibRfidInterval.setStatus('current')
if mibBuilder.loadTexts: cLD11ClientCalibRfidInterval.setDescription('This object specifies the notification interval for RFID tags.')
cLD11ClientCalibRogueInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 522, 1, 1, 20), Unsigned32()).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLD11ClientCalibRogueInterval.setStatus('current')
if mibBuilder.loadTexts: cLD11ClientCalibRogueInterval.setDescription('This object specifies the notification interval for Rogue APs and Rogue clients.')
ciscoLwappDot11ClientCalibMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 522, 2, 1))
ciscoLwappDot11ClientCalibMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 522, 2, 2))
ciscoLwappDot11ClientCalibMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 522, 2, 1, 1)).setObjects(("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "ciscoLwappDot11ClientCalibMIBConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappDot11ClientCalibMIBCompliance = ciscoLwappDot11ClientCalibMIBCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: ciscoLwappDot11ClientCalibMIBCompliance.setDescription('The compliance statement for the SNMP entities that implement this MIB.')
ciscoLwappDot11ClientCalibMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 522, 2, 1, 2)).setObjects(("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibClientConfigGroup"), ("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibGlobalConfigGroup"), ("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibRssiDataSampleGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappDot11ClientCalibMIBComplianceRev1 = ciscoLwappDot11ClientCalibMIBComplianceRev1.setStatus('current')
if mibBuilder.loadTexts: ciscoLwappDot11ClientCalibMIBComplianceRev1.setDescription('The compliance statement for the SNMP entities that implement this MIB.')
ciscoLwappDot11ClientCalibMIBConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 522, 2, 2, 1)).setObjects(("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibBeaconInterval"), ("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibRowStatus"), ("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibTableMaxEntries"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappDot11ClientCalibMIBConfigGroup = ciscoLwappDot11ClientCalibMIBConfigGroup.setStatus('deprecated')
if mibBuilder.loadTexts: ciscoLwappDot11ClientCalibMIBConfigGroup.setDescription('This collection of objects specifies the required calibration parameters for the 802.11 wireless clients. ciscoLwappDot11ClientCalibMIBConfigGroup object is superseded by cLD11ClientCalibClientConfigGroup.')
cLD11ClientCalibClientConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 522, 2, 2, 2)).setObjects(("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibRowStatus"), ("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibBeaconIntervalExt"), ("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibNumberOfRadios"), ("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibNumberOfSamples"), ("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibSamplesCollected"), ("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibStorageType"), ("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibTableMaxEntries"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cLD11ClientCalibClientConfigGroup = cLD11ClientCalibClientConfigGroup.setStatus('current')
if mibBuilder.loadTexts: cLD11ClientCalibClientConfigGroup.setDescription('This collection of objects providing the required calibration parameters for the 802.11 wireless clients.')
cLD11ClientCalibGlobalConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 522, 2, 2, 3)).setObjects(("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibRssiAlgorithm"), ("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibRssiClientExpiryTimeout"), ("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibRssiCalibClientExpiryTimeout"), ("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibRssiRfidTagExpiryTimeout"), ("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibRssiRogueApExpiryTimeout"), ("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibRssiClientHalflifeTimeout"), ("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibRssiCalibClientHalflifeTimeout"), ("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibRssiRfidTagHalflifeTimeout"), ("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibRssiRogueApHalflifeTimeout"), ("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibRfidDataEnable"), ("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibRfidTimeout"), ("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibClientMultiBandEnable"), ("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibClientRequestEnable"), ("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibClientBurstIntervalEnable"), ("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibClientBurstInterval"), ("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibClientInterval"), ("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibRfidInterval"), ("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "cLD11ClientCalibRogueInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cLD11ClientCalibGlobalConfigGroup = cLD11ClientCalibGlobalConfigGroup.setStatus('current')
if mibBuilder.loadTexts: cLD11ClientCalibGlobalConfigGroup.setDescription('This collection of objects providing the required RSSI calibration parameters for the 802.11 wireless clients.')
cLD11ClientCalibRssiDataSampleGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 522, 2, 2, 4)).setObjects(("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "clD11ClientCalibDataRssiValue"), ("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", "clD11ClientCalibDataTransmitPower"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cLD11ClientCalibRssiDataSampleGroup = cLD11ClientCalibRssiDataSampleGroup.setStatus('current')
if mibBuilder.loadTexts: cLD11ClientCalibRssiDataSampleGroup.setDescription('This collection of objects providing the RSSI data samples collected for 802.11 client.')
mibBuilder.exportSymbols("CISCO-LWAPP-DOT11-CLIENT-CALIB-MIB", cLD11ClientCalibClientBurstInterval=cLD11ClientCalibClientBurstInterval, cLD11ClientCalibRfidInterval=cLD11ClientCalibRfidInterval, ciscoLwappDot11ClientCalibMIBConfigGroup=ciscoLwappDot11ClientCalibMIBConfigGroup, cLD11ClientCalibRssiRogueApHalflifeTimeout=cLD11ClientCalibRssiRogueApHalflifeTimeout, cLD11ClientCalibRssiClientExpiryTimeout=cLD11ClientCalibRssiClientExpiryTimeout, ciscoLwappDot11ClientCalibMIBNotifs=ciscoLwappDot11ClientCalibMIBNotifs, cLD11ClientCalibClientBurstIntervalEnable=cLD11ClientCalibClientBurstIntervalEnable, ciscoLwappDot11ClientCalibMIBGroups=ciscoLwappDot11ClientCalibMIBGroups, cLD11ClientCalibRssiRogueApExpiryTimeout=cLD11ClientCalibRssiRogueApExpiryTimeout, cLD11ClientCalibMacAddress=cLD11ClientCalibMacAddress, cLD11ClientCalibClientRequestEnable=cLD11ClientCalibClientRequestEnable, cLD11ClientCalibBeaconIntervalExt=cLD11ClientCalibBeaconIntervalExt, cLD11ClientCalibClientConfigGroup=cLD11ClientCalibClientConfigGroup, ciscoLwappDot11ClientCalibMIBConform=ciscoLwappDot11ClientCalibMIBConform, cLD11ClientCalibRfidDataEnable=cLD11ClientCalibRfidDataEnable, cldccRssiSamples=cldccRssiSamples, cLD11ClientCalibRssiAlgorithm=cLD11ClientCalibRssiAlgorithm, cLD11ClientCalibRssiClientHalflifeTimeout=cLD11ClientCalibRssiClientHalflifeTimeout, cLD11ClientCalibRssiRfidTagHalflifeTimeout=cLD11ClientCalibRssiRfidTagHalflifeTimeout, clD11ClientCalibDataRssiValue=clD11ClientCalibDataRssiValue, cldccConfig=cldccConfig, cLD11ClientCalibSamplesCollected=cLD11ClientCalibSamplesCollected, cLD11ClientCalibDataTable=cLD11ClientCalibDataTable, ciscoLwappDot11ClientCalibMIB=ciscoLwappDot11ClientCalibMIB, cLD11ClientCalibClientMultiBandEnable=cLD11ClientCalibClientMultiBandEnable, cLD11ClientCalibRssiDataSampleGroup=cLD11ClientCalibRssiDataSampleGroup, cLD11ClientCalibEntry=cLD11ClientCalibEntry, cLD11ClientCalibTable=cLD11ClientCalibTable, clD11ClientCalibDataTimeStamp=clD11ClientCalibDataTimeStamp, cLD11ClientCalibRowStatus=cLD11ClientCalibRowStatus, PYSNMP_MODULE_ID=ciscoLwappDot11ClientCalibMIB, cLD11ClientCalibGlobalConfigGroup=cLD11ClientCalibGlobalConfigGroup, clD11ClientCalibDataTransmitPower=clD11ClientCalibDataTransmitPower, cLD11ClientCalibRssiRfidTagExpiryTimeout=cLD11ClientCalibRssiRfidTagExpiryTimeout, cLD11ClientCalibDataEntry=cLD11ClientCalibDataEntry, ciscoLwappDot11ClientCalibMIBCompliances=ciscoLwappDot11ClientCalibMIBCompliances, clD11ClientCalibDataAntennaIndex=clD11ClientCalibDataAntennaIndex, cLD11ClientCalibStorageType=cLD11ClientCalibStorageType, cLD11ClientCalibRssiCalibClientHalflifeTimeout=cLD11ClientCalibRssiCalibClientHalflifeTimeout, ciscoLwappDot11ClientCalibMIBCompliance=ciscoLwappDot11ClientCalibMIBCompliance, cLD11ClientCalibRssiCalibClientExpiryTimeout=cLD11ClientCalibRssiCalibClientExpiryTimeout, cLD11ClientCalibClientInterval=cLD11ClientCalibClientInterval, cLD11ClientCalibTableMaxEntries=cLD11ClientCalibTableMaxEntries, cLD11ClientCalibRfidTimeout=cLD11ClientCalibRfidTimeout, ciscoLwappDot11ClientCalibMIBObjects=ciscoLwappDot11ClientCalibMIBObjects, cldccStatus=cldccStatus, cLD11ClientCalibNumberOfSamples=cLD11ClientCalibNumberOfSamples, cLD11ClientCalibRogueInterval=cLD11ClientCalibRogueInterval, ciscoLwappDot11ClientCalibMIBComplianceRev1=ciscoLwappDot11ClientCalibMIBComplianceRev1, cLD11ClientCalibBeaconInterval=cLD11ClientCalibBeaconInterval, cLD11ClientCalibNumberOfRadios=cLD11ClientCalibNumberOfRadios)
