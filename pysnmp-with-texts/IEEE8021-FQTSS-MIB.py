#
# PySNMP MIB module IEEE8021-FQTSS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IEEE8021-FQTSS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:52:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ieee8021BridgeBaseComponentId, ieee8021BridgeBasePort = mibBuilder.importSymbols("IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId", "ieee8021BridgeBasePort")
IEEE8021PriorityValue, ieee802dot1mibs = mibBuilder.importSymbols("IEEE8021-TC-MIB", "IEEE8021PriorityValue", "ieee802dot1mibs")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
IpAddress, Gauge32, ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ModuleIdentity, Counter64, Unsigned32, NotificationType, iso, Bits, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Gauge32", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ModuleIdentity", "Counter64", "Unsigned32", "NotificationType", "iso", "Bits", "TimeTicks", "Integer32")
TruthValue, TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "RowStatus", "DisplayString")
ieee8021FqtssMib = ModuleIdentity((1, 3, 111, 2, 802, 1, 1, 16))
ieee8021FqtssMib.setRevisions(('2014-12-15 00:00', '2011-02-27 00:00', '2009-10-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ieee8021FqtssMib.setRevisionsDescriptions(('Published as part of IEEE Std 802.1Q 2014 revision. Cross references updated and corrected.', 'Minor edits to contact information etc. as part of 2011 revision of IEEE Std 802.1Q.', 'Initial revision, included in IEEE 802.1Qav.',))
if mibBuilder.loadTexts: ieee8021FqtssMib.setLastUpdated('201412150000Z')
if mibBuilder.loadTexts: ieee8021FqtssMib.setOrganization('IEEE 802.1 Working Group')
if mibBuilder.loadTexts: ieee8021FqtssMib.setContactInfo(' WG-URL: http://grouper.ieee.org/groups/802/1/index.html WG-EMail: stds-802-1@ieee.org Contact: IEEE 802.1 Working Group Chair Postal: C/O IEEE 802.1 Working Group IEEE Standards Association 445 Hoes Lane P.O. Box 1331 Piscataway NJ 08855-1331 USA E-mail: STDS-802-1-L@LISTSERV.IEEE.ORG')
if mibBuilder.loadTexts: ieee8021FqtssMib.setDescription('The Bridge MIB module for managing devices that support the Forwarding and Queuing Enhancements for Time Sensitive Streams. Unless otherwise indicated, the references in this MIB module are to IEEE Std 802.1Q-2014. Copyright (C) IEEE (2014). This version of this MIB module is part of IEEE802.1Q; see the draft itself for full legal notices.')
class IEEE8021FqtssTrafficClassValue(TextualConvention, Unsigned32):
    reference = '12.20.1'
    description = 'An 802.1 FQTSS traffic class value. This is the numerical value associated with a traffic class in a Bridge. Larger values are associated with higher priority traffic classes.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 7)

class IEEE8021FqtssDeltaBandwidthValue(TextualConvention, Unsigned32):
    reference = '12.20.1, 34.4'
    description = 'An 802.1 FQTSS delta bandwidth percentage, represented as a fixed point number scaled by 1,000,000.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 100000000)

class IEEE8021FqtssTxSelectionAlgorithmIDValue(TextualConvention, Unsigned32):
    reference = '8.6.8, 12.20.2'
    description = 'An 802.1 transmission selection algorithm identifier value. This is an integer, with the following interpretation placed on the value: 0: Strict priority algorithm, 1: Credit-based shaper algorithm, 2-255: Reserved for future standardization, 256-4294967295: Vendor-specific transmission selection algorithm identifiers, consisting of a four-octet integer, where the most significant 3 octets hold an OUI or CID value, and the least significant octet holds an integer value in the range 0-255 assigned by the owner of the OUI or CID.'
    status = 'current'
    displayHint = 'd'

ieee8021FqtssNotifications = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 16, 0))
ieee8021FqtssObjects = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 16, 1))
ieee8021FqtssConformance = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 16, 2))
ieee8021FqtssBap = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 16, 1, 1))
ieee8021FqtssMappings = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 16, 1, 2))
ieee8021FqtssBapTable = MibTable((1, 3, 111, 2, 802, 1, 1, 16, 1, 1, 1), )
if mibBuilder.loadTexts: ieee8021FqtssBapTable.setReference('12.20.1')
if mibBuilder.loadTexts: ieee8021FqtssBapTable.setStatus('current')
if mibBuilder.loadTexts: ieee8021FqtssBapTable.setDescription('A table containing a set of bandwidth availability parameters for each traffic class that supports the credit-based shaper algorithm. All writable objects in this table must be persistent over power up restart/reboot.')
ieee8021FqtssBapEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 16, 1, 1, 1, 1), ).setIndexNames((0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"), (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"), (0, "IEEE8021-FQTSS-MIB", "ieee8021FqtssBAPTrafficClass"))
if mibBuilder.loadTexts: ieee8021FqtssBapEntry.setStatus('current')
if mibBuilder.loadTexts: ieee8021FqtssBapEntry.setDescription('A list of objects containing bandwidth allocation information for each traffic class that supports the credit-based shaper algorithm. Rows in the table are automatically created and deleted as a result of the operation of the algorithm described in 34.5. ')
ieee8021FqtssBAPTrafficClass = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 16, 1, 1, 1, 1, 1), IEEE8021FqtssTrafficClassValue())
if mibBuilder.loadTexts: ieee8021FqtssBAPTrafficClass.setReference('12.20.2, 34.3, 34.5')
if mibBuilder.loadTexts: ieee8021FqtssBAPTrafficClass.setStatus('current')
if mibBuilder.loadTexts: ieee8021FqtssBAPTrafficClass.setDescription('The traffic class number associated with the row of the table. A row in this table is created for each traffic class that supports the credit-based shaper algrithm. The recommended mappings of priorities to traffic classes for support of the credit-based shaper algorithm are described in 34.5.')
ieee8021FqtssDeltaBandwidth = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 16, 1, 1, 1, 1, 2), IEEE8021FqtssDeltaBandwidthValue()).setUnits('percent').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021FqtssDeltaBandwidth.setReference('12.20.1, 34.3')
if mibBuilder.loadTexts: ieee8021FqtssDeltaBandwidth.setStatus('current')
if mibBuilder.loadTexts: ieee8021FqtssDeltaBandwidth.setDescription('The value of the deltaBandwidth parameter for the traffic class. This value is represented as a fixed point number scaled by a factor of 1,000,000; i.e., 100,000,000 (the maximum value) represents 100%. The default value of the deltaBandwidth parameter for the highest numbered traffic class that supports the credit-based shaper algorithm is 75%; for all lower numbered traffic classes that support the credit-based shaper algorithm the default value is 0%. The value of this object MUST be retained across reinitializations of the management system.')
ieee8021FqtssOperIdleSlopeMs = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 16, 1, 1, 1, 1, 3), Unsigned32()).setUnits('bits per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021FqtssOperIdleSlopeMs.setReference('12.20.1, 34.3')
if mibBuilder.loadTexts: ieee8021FqtssOperIdleSlopeMs.setStatus('current')
if mibBuilder.loadTexts: ieee8021FqtssOperIdleSlopeMs.setDescription('The most significant 32 bits of the bandwidth, in bits per second, that is currently allocated to the traffic class (idleSlope(N)). This object MUST be read at the same time as ieee8021FqtssOperIdleSlopeLs, which represents the LS 32 bits of the value, in order for the read operation to succeed. If SRP is supported and in operation, then the reserved bandwidth is determined by the operation of SRP; otherwise, the value of ieee8021FqtssOperIdleSlopeMs is equal to the value of ieee8021FqtssAdminIdleSlopeMs. The value of this object MUST be retained across reinitializations of the management system.')
ieee8021FqtssOperIdleSlopeLs = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 16, 1, 1, 1, 1, 4), Unsigned32()).setUnits('bits per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021FqtssOperIdleSlopeLs.setReference('12.20.1, 34.3')
if mibBuilder.loadTexts: ieee8021FqtssOperIdleSlopeLs.setStatus('current')
if mibBuilder.loadTexts: ieee8021FqtssOperIdleSlopeLs.setDescription('The least significant 32 bits of the bandwidth, in bits per second, that is currently allocated to the traffic class (idleSlope(N)). This object MUST be read at the same time as ieee8021FqtssOperIdleSlopeMs, which represents the LS 32 bits of the value, in order for the read operation to succeed. If SRP is supported and in operation, then the reserved bandwidth is determined by the operation of SRP; otherwise, the value of ieee8021FqtssOperIdleSlopeLs is equal to the value of ieee8021FqtssAdminIdleSlopeMs. The value of this object MUST be retained across reinitializations of the management system.')
ieee8021FqtssAdminIdleSlopeMs = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 16, 1, 1, 1, 1, 5), Unsigned32()).setUnits('bits per second').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021FqtssAdminIdleSlopeMs.setReference('12.20.1, 34.3')
if mibBuilder.loadTexts: ieee8021FqtssAdminIdleSlopeMs.setStatus('current')
if mibBuilder.loadTexts: ieee8021FqtssAdminIdleSlopeMs.setDescription('The most significant 32 bits of the bandwidth, in bits per second, that the manager desires to allocate to the traffic class as idleSlope(N). This object MUST be read or written at the same time as ieee8021FqtssAdminIdleSlopeLs, which represents the LS 32 bits of the value, in order for the read or write operation to succeed. If SRP is supported and in operation, then the reserved bandwidth is determined by the operation of SRP, and any changes to the value of this object have no effect on the operational value of idleSlope(N). The value of this object MUST be retained across reinitializations of the management system.')
ieee8021FqtssAdminIdleSlopeLs = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 16, 1, 1, 1, 1, 6), Unsigned32()).setUnits('bits per second').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021FqtssAdminIdleSlopeLs.setReference('12.20.1, 34.3')
if mibBuilder.loadTexts: ieee8021FqtssAdminIdleSlopeLs.setStatus('current')
if mibBuilder.loadTexts: ieee8021FqtssAdminIdleSlopeLs.setDescription('The least significant 32 bits of the bandwidth, in bits per second, that the manager desires to allocate to the traffic class as idleSlope(N). This object MUST be read or written at the same time as ieee8021FqtssAdminIdleSlopeMs, which represents the LS 32 bits of the value, in order for the read or write operation to succeed. If SRP is supported and in operation, then the reserved bandwidth is determined by the operation of SRP, and any changes to the value of this object have no effect on the operational value of idleSlope(N). The value of this object MUST be retained across reinitializations of the management system.')
ieee8021FqtssBapRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 16, 1, 1, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021FqtssBapRowStatus.setStatus('current')
if mibBuilder.loadTexts: ieee8021FqtssBapRowStatus.setDescription('Indicates the status of an entry (row) in this table, and is used to create/delete entries. The corresponding instances of the following objects must be set before this object can be made active(1): ieee8021FqtssBAPTrafficClass ieee8021FqtssDeltaBandwidth ieee8021FqtssOperIdleSlopeMs ieee8021FqtssOperIdleSlopeLs ieee8021FqtssAdminIdleSlopeMs ieee8021FqtssAdminIdleSlopeLs The corresponding instances of the following objects may not be changed while this object is active(1): ieee8021FqtssBAPTrafficClass')
ieee8021FqtssTxSelectionAlgorithmTable = MibTable((1, 3, 111, 2, 802, 1, 1, 16, 1, 2, 1), )
if mibBuilder.loadTexts: ieee8021FqtssTxSelectionAlgorithmTable.setReference('8.6.8, 12.20.2, 34.5')
if mibBuilder.loadTexts: ieee8021FqtssTxSelectionAlgorithmTable.setStatus('current')
if mibBuilder.loadTexts: ieee8021FqtssTxSelectionAlgorithmTable.setDescription('A table containing the assignment of transmission selection algorithms to traffic classes for the Port. This table provides management of the Transmission Selection Algorithm Table defined in 8.6.8. For a given Port, a row in the table exists for each traffic class that is supported by the Port. The default assignments of transmission selection algorithms to traffic classes in the table are made on instantiation of the table, in accordance with the defaults defined in 8.6.8 and 34.5. All writable objects in this table must be persistent over power up restart/reboot.')
ieee8021FqtssTxSelectionAlgorithmEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 16, 1, 2, 1, 1), ).setIndexNames((0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"), (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"), (0, "IEEE8021-FQTSS-MIB", "ieee8021FqtssTrafficClass"))
if mibBuilder.loadTexts: ieee8021FqtssTxSelectionAlgorithmEntry.setStatus('current')
if mibBuilder.loadTexts: ieee8021FqtssTxSelectionAlgorithmEntry.setDescription('A list of objects that contain the mapping of a traffic class value to a transmission selection algorithm value.')
ieee8021FqtssTrafficClass = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 16, 1, 2, 1, 1, 1), IEEE8021FqtssTrafficClassValue())
if mibBuilder.loadTexts: ieee8021FqtssTrafficClass.setReference('8.6.8, 12.20.2, 34.5')
if mibBuilder.loadTexts: ieee8021FqtssTrafficClass.setStatus('current')
if mibBuilder.loadTexts: ieee8021FqtssTrafficClass.setDescription('The traffic class to which the transmission selection algorithm is assigned. The value of this object MUST be retained across reinitializations of the management system.')
ieee8021FqtssTxSelectionAlgorithmID = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 16, 1, 2, 1, 1, 2), IEEE8021FqtssTxSelectionAlgorithmIDValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021FqtssTxSelectionAlgorithmID.setReference('8.6.8, 12.20.2, 34.5')
if mibBuilder.loadTexts: ieee8021FqtssTxSelectionAlgorithmID.setStatus('current')
if mibBuilder.loadTexts: ieee8021FqtssTxSelectionAlgorithmID.setDescription('The identifier of the transmission selection algorithm assigned to the traffic class. The value of this object MUST be retained across reinitializations of the management system.')
ieee8021FqtssSrpRegenOverrideTable = MibTable((1, 3, 111, 2, 802, 1, 1, 16, 1, 2, 2), )
if mibBuilder.loadTexts: ieee8021FqtssSrpRegenOverrideTable.setReference('35.1.4, 6.9.4, 12.20.3')
if mibBuilder.loadTexts: ieee8021FqtssSrpRegenOverrideTable.setStatus('current')
if mibBuilder.loadTexts: ieee8021FqtssSrpRegenOverrideTable.setDescription('A table containing the set of priority regeneration table override values for the Port. The recommended default values of priorities associated with SR classes, and the corresponding override values, are defined in 6.9.4. All writable objects in this table must be persistent over power up restart/reboot.')
ieee8021FqtssSrpRegenOverrideEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 16, 1, 2, 2, 1), ).setIndexNames((0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"), (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"), (0, "IEEE8021-FQTSS-MIB", "ieee8021FqtssSrClassPriority"))
if mibBuilder.loadTexts: ieee8021FqtssSrpRegenOverrideEntry.setStatus('current')
if mibBuilder.loadTexts: ieee8021FqtssSrpRegenOverrideEntry.setDescription('A list of objects that contain the mapping of a priority value to a priority regeneration override value, and a boundary port indication. Rows in the table exist for all priorities that are associated with SR classes.')
ieee8021FqtssSrClassPriority = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 16, 1, 2, 2, 1, 1), IEEE8021PriorityValue())
if mibBuilder.loadTexts: ieee8021FqtssSrClassPriority.setReference('35.1.4, 6.9.4, 12.20.3')
if mibBuilder.loadTexts: ieee8021FqtssSrClassPriority.setStatus('current')
if mibBuilder.loadTexts: ieee8021FqtssSrClassPriority.setDescription('The priority value that is overridden at the SRP domain boundary. ')
ieee8021FqtssPriorityRegenOverride = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 16, 1, 2, 2, 1, 2), IEEE8021PriorityValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021FqtssPriorityRegenOverride.setReference('35.1.4, 6.9.4, 12.20.3')
if mibBuilder.loadTexts: ieee8021FqtssPriorityRegenOverride.setStatus('current')
if mibBuilder.loadTexts: ieee8021FqtssPriorityRegenOverride.setDescription('The priority value that is used to override the priority regeneration table entry at the SRP domain boundary. The value of this object MUST be retained across reinitializations of the management system.')
ieee8021FqtssSrpBoundaryPort = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 16, 1, 2, 2, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021FqtssSrpBoundaryPort.setReference('35.1.4, 6.9.4, 12.20.3')
if mibBuilder.loadTexts: ieee8021FqtssSrpBoundaryPort.setStatus('current')
if mibBuilder.loadTexts: ieee8021FqtssSrpBoundaryPort.setDescription('The value of the SRPdomainBoundaryPort parameter (35.1.4) for the priority. ')
ieee8021FqtssCompliances = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 16, 2, 1))
ieee8021FqtssGroups = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 16, 2, 2))
ieee8021FqtssBapGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 16, 2, 2, 1)).setObjects(("IEEE8021-FQTSS-MIB", "ieee8021FqtssDeltaBandwidth"), ("IEEE8021-FQTSS-MIB", "ieee8021FqtssOperIdleSlopeMs"), ("IEEE8021-FQTSS-MIB", "ieee8021FqtssOperIdleSlopeLs"), ("IEEE8021-FQTSS-MIB", "ieee8021FqtssAdminIdleSlopeMs"), ("IEEE8021-FQTSS-MIB", "ieee8021FqtssAdminIdleSlopeLs"), ("IEEE8021-FQTSS-MIB", "ieee8021FqtssBapRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021FqtssBapGroup = ieee8021FqtssBapGroup.setStatus('current')
if mibBuilder.loadTexts: ieee8021FqtssBapGroup.setDescription('Objects that define bandwidth allocation for FQTSS.')
ieee8021FqtssTxSelectionAlgorithmGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 16, 2, 2, 2)).setObjects(("IEEE8021-FQTSS-MIB", "ieee8021FqtssTxSelectionAlgorithmID"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021FqtssTxSelectionAlgorithmGroup = ieee8021FqtssTxSelectionAlgorithmGroup.setStatus('current')
if mibBuilder.loadTexts: ieee8021FqtssTxSelectionAlgorithmGroup.setDescription('Objects that define transmission selection mappings for FQTSS.')
ieee8021FqtssBoundaryPortGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 16, 2, 2, 3)).setObjects(("IEEE8021-FQTSS-MIB", "ieee8021FqtssPriorityRegenOverride"), ("IEEE8021-FQTSS-MIB", "ieee8021FqtssSrpBoundaryPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021FqtssBoundaryPortGroup = ieee8021FqtssBoundaryPortGroup.setStatus('current')
if mibBuilder.loadTexts: ieee8021FqtssBoundaryPortGroup.setDescription('Objects that define boundary port priority override mappings for FQTSS.')
ieee8021FqtssCompliance = ModuleCompliance((1, 3, 111, 2, 802, 1, 1, 16, 2, 1, 1)).setObjects(("IEEE8021-FQTSS-MIB", "ieee8021FqtssBapGroup"), ("IEEE8021-FQTSS-MIB", "ieee8021FqtssTxSelectionAlgorithmGroup"), ("IEEE8021-FQTSS-MIB", "ieee8021FqtssBoundaryPortGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021FqtssCompliance = ieee8021FqtssCompliance.setStatus('current')
if mibBuilder.loadTexts: ieee8021FqtssCompliance.setDescription('The compliance statement for devices supporting forwarding and queuing for time sensitive streams. Support of the objects defined in the IEEE8021-FQTSS MIB also requires support of the IEEE8021-BRIDGE-MIB; the provisions of 17.3.2 apply to implementations claiming support of the IEEE8021-FQTSS MIB. ')
mibBuilder.exportSymbols("IEEE8021-FQTSS-MIB", ieee8021FqtssBAPTrafficClass=ieee8021FqtssBAPTrafficClass, ieee8021FqtssBapRowStatus=ieee8021FqtssBapRowStatus, ieee8021FqtssNotifications=ieee8021FqtssNotifications, ieee8021FqtssBapGroup=ieee8021FqtssBapGroup, ieee8021FqtssPriorityRegenOverride=ieee8021FqtssPriorityRegenOverride, ieee8021FqtssBapTable=ieee8021FqtssBapTable, ieee8021FqtssAdminIdleSlopeMs=ieee8021FqtssAdminIdleSlopeMs, ieee8021FqtssConformance=ieee8021FqtssConformance, IEEE8021FqtssDeltaBandwidthValue=IEEE8021FqtssDeltaBandwidthValue, ieee8021FqtssAdminIdleSlopeLs=ieee8021FqtssAdminIdleSlopeLs, ieee8021FqtssCompliance=ieee8021FqtssCompliance, ieee8021FqtssOperIdleSlopeLs=ieee8021FqtssOperIdleSlopeLs, PYSNMP_MODULE_ID=ieee8021FqtssMib, ieee8021FqtssTxSelectionAlgorithmTable=ieee8021FqtssTxSelectionAlgorithmTable, ieee8021FqtssMappings=ieee8021FqtssMappings, ieee8021FqtssBapEntry=ieee8021FqtssBapEntry, ieee8021FqtssTrafficClass=ieee8021FqtssTrafficClass, ieee8021FqtssBap=ieee8021FqtssBap, ieee8021FqtssSrpRegenOverrideTable=ieee8021FqtssSrpRegenOverrideTable, ieee8021FqtssCompliances=ieee8021FqtssCompliances, ieee8021FqtssBoundaryPortGroup=ieee8021FqtssBoundaryPortGroup, ieee8021FqtssDeltaBandwidth=ieee8021FqtssDeltaBandwidth, ieee8021FqtssGroups=ieee8021FqtssGroups, ieee8021FqtssMib=ieee8021FqtssMib, ieee8021FqtssTxSelectionAlgorithmID=ieee8021FqtssTxSelectionAlgorithmID, ieee8021FqtssTxSelectionAlgorithmGroup=ieee8021FqtssTxSelectionAlgorithmGroup, ieee8021FqtssOperIdleSlopeMs=ieee8021FqtssOperIdleSlopeMs, ieee8021FqtssSrpRegenOverrideEntry=ieee8021FqtssSrpRegenOverrideEntry, IEEE8021FqtssTxSelectionAlgorithmIDValue=IEEE8021FqtssTxSelectionAlgorithmIDValue, ieee8021FqtssSrClassPriority=ieee8021FqtssSrClassPriority, IEEE8021FqtssTrafficClassValue=IEEE8021FqtssTrafficClassValue, ieee8021FqtssSrpBoundaryPort=ieee8021FqtssSrpBoundaryPort, ieee8021FqtssObjects=ieee8021FqtssObjects, ieee8021FqtssTxSelectionAlgorithmEntry=ieee8021FqtssTxSelectionAlgorithmEntry)
