#
# PySNMP MIB module CISCO-DOT11-ANTENNA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DOT11-ANTENNA-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:55:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, NotificationType, ObjectIdentity, iso, ModuleIdentity, MibIdentifier, Bits, Gauge32, Unsigned32, Counter64, Counter32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "NotificationType", "ObjectIdentity", "iso", "ModuleIdentity", "MibIdentifier", "Bits", "Gauge32", "Unsigned32", "Counter64", "Counter32", "Integer32")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
ciscoDot11AntennaMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 384))
ciscoDot11AntennaMIB.setRevisions(('2016-02-15 00:00', '2003-12-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoDot11AntennaMIB.setRevisionsDescriptions(('Changed ciscoDot11AntennaMIB OID from 3333 to 384. ', 'Initial version of this MIB module. ',))
if mibBuilder.loadTexts: ciscoDot11AntennaMIB.setLastUpdated('201602150000Z')
if mibBuilder.loadTexts: ciscoDot11AntennaMIB.setOrganization('Cisco System Inc.')
if mibBuilder.loadTexts: ciscoDot11AntennaMIB.setContactInfo(' Cisco Systems, Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-dot11@cisco.com')
if mibBuilder.loadTexts: ciscoDot11AntennaMIB.setDescription("This MIB is intended to be implemented on 802.11 Access Points and Wireless Bridges to provide information about the antennas connected to their 802.11 interfaces. The NMS retrieves the configured antenna parameters and uses it to calculate the recommended radio settings to be applied to the Access Points being managed to achieve optimum coverage and throughput. GLOSSARY Access Point ( AP ) An entity that contains an 802.11 medium access control ( MAC ) and physical layer ( PHY ) interface and provides access to the distribution services via the wireless medium for associated clients. Wireless Bridge An 802.11 entity that provides wireless connectivity between two wired LAN segments and is used in point- to-point or point-multipoint configurations. Repeater-AP A repeater is a 'wireless AP' that is attached to a parent AP on an 802.11 primary port. The Ethernet port is disabled in a Repeater-AP. Antenna A passive device connected to the 802.11 interface that is used for transmission and reception of the radio signals. Antennas transmit radio signals in all directions (omnidirectional) or in a particular direction(directional, high-gain). Antenna Gain The Antenna Gain is the measure of the amount of amplification done on the input radio signal by the antenna. Amplification is done by virtue of focussing the RF radiation into a tighter beam. Antenna Gain is expressed as dBi units. Attenuator An attenuator circuit allows a known source of power to be reduced by a predetermined factor usually expressed as decibels. This power reduction is achieved by the attenuator without introducing distortion. An attenuator may be used in either audio or radio signal circuits. ")
cDot11AntennaMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 384, 1))
cDot11AntennaGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 384, 1, 1))
cDot11AntennaTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 384, 1, 1, 1), )
if mibBuilder.loadTexts: cDot11AntennaTable.setStatus('current')
if mibBuilder.loadTexts: cDot11AntennaTable.setDescription('This table holds the specification of the antenna connected to the 802.11 interfaces of an infrastructure device like an AP or Bridge. The table gets populated when the administrator configures the 802.11 interface with information about the antenna connected to it. This table has a sparse dependent relationship with ifTable defined in IF-MIB. There exists an entry in this table corresponding to the entry for each dot11 interface found in ifTable. This table is not applicable to virtual dot11 interfaces. ')
cDot11AntennaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 384, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cDot11AntennaEntry.setStatus('current')
if mibBuilder.loadTexts: cDot11AntennaEntry.setDescription('An entry corresponds to the set of operational parameters of the antenna connected to the 802.11 interface identified by ifIndex. ')
cDot11AntennaIsGainConfigured = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 384, 1, 1, 1, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11AntennaIsGainConfigured.setStatus('current')
if mibBuilder.loadTexts: cDot11AntennaIsGainConfigured.setDescription("This flag indicates whether the 802.11 interface is connected to an external antenna and/or the attenuator and configured with the resultant gain or not. If the interface has an external antenna and/or an attenuator connected to it and has been configured with the resultant gain, the value of this object is 'true'. This object, when 'false', indicates that both the external antenna and the attenuator are physically disconnected from the 802.11 interface. Also, the query to the object cDot11AntennaResultantGain returns the default gain corresponding to the PHY type of that 802.11 interface when this object's value is 'false'. ")
cDot11AntennaResultantGain = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 384, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-128, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11AntennaResultantGain.setStatus('current')
if mibBuilder.loadTexts: cDot11AntennaResultantGain.setDescription("This object, expressed in dB, is used to calculate the appropriate radio settings for the wireless infrastructure devices being managed. The semantics are as follows. For a dot11 interface without an external antenna and an attenuator connected to it, the value of this object is the default gain corresponding to the PHY type of that respective interface. If the particular dot11 interface is connected to an external antenna in the presence of an attenuator, this object holds the value that is the resultant of the gain of the antenna as specified by the antenna's hardware specification and the attenuation introduced by the attenuator, as configured by the administrator. In the absence of an attenuator, the value held by this object is the exact value of the gain of the external antenna configured by the administrator as specified by the antenna's hardware specification, if an external antenna is connected to the 802.11 interface. In the absence of an external antenna, if the attenuator is present, the value of this object is is the amount of attenuation that is intended to be introduced to control the output power, as configured by the administrator. The value of this object is reverted back by the agent to the default gain corresponding to the PHY type of the particular 802.11 interface, when both the external antenna and the attenuator are physically disconnected from the particular interface and the gain configured earlier is cleared by the administrator. ")
cDot11AntennaMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 384, 2))
cDot11AntennaMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 384, 2, 1))
cDot11AntennaMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 384, 2, 2))
cDot11AntennaMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 384, 2, 1, 1)).setObjects(("CISCO-DOT11-ANTENNA-MIB", "cDot11AntennaGlobalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDot11AntennaMIBCompliance = cDot11AntennaMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: cDot11AntennaMIBCompliance.setDescription('The compliance statement for the SNMP entities that implement the ciscoDot11AntennaMIB module.')
cDot11AntennaGlobalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 384, 2, 2, 1)).setObjects(("CISCO-DOT11-ANTENNA-MIB", "cDot11AntennaIsGainConfigured"), ("CISCO-DOT11-ANTENNA-MIB", "cDot11AntennaResultantGain"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDot11AntennaGlobalGroup = cDot11AntennaGlobalGroup.setStatus('current')
if mibBuilder.loadTexts: cDot11AntennaGlobalGroup.setDescription('This collection of objects provide information about the antenna connected to the 802.11 interfaces of a WLAN infrastructure device like an Access Point or a Bridge. ')
mibBuilder.exportSymbols("CISCO-DOT11-ANTENNA-MIB", cDot11AntennaTable=cDot11AntennaTable, cDot11AntennaResultantGain=cDot11AntennaResultantGain, cDot11AntennaGlobal=cDot11AntennaGlobal, cDot11AntennaMIBCompliances=cDot11AntennaMIBCompliances, cDot11AntennaMIBGroups=cDot11AntennaMIBGroups, cDot11AntennaMIBCompliance=cDot11AntennaMIBCompliance, cDot11AntennaMIBConform=cDot11AntennaMIBConform, cDot11AntennaEntry=cDot11AntennaEntry, cDot11AntennaGlobalGroup=cDot11AntennaGlobalGroup, PYSNMP_MODULE_ID=ciscoDot11AntennaMIB, cDot11AntennaMIBObjects=cDot11AntennaMIBObjects, cDot11AntennaIsGainConfigured=cDot11AntennaIsGainConfigured, ciscoDot11AntennaMIB=ciscoDot11AntennaMIB)
