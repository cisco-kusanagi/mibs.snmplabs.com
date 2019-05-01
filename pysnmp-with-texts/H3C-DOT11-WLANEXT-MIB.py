#
# PySNMP MIB module H3C-DOT11-WLANEXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-DOT11-WLANEXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:21:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
H3cDot11ObjectIDType, h3cDot11, H3cDot11QosAcType, H3cDot11RadioScopeType = mibBuilder.importSymbols("H3C-DOT11-REF-MIB", "H3cDot11ObjectIDType", "h3cDot11", "H3cDot11QosAcType", "H3cDot11RadioScopeType")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Gauge32, iso, IpAddress, MibIdentifier, TimeTicks, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, ObjectIdentity, Counter64, Counter32, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Gauge32", "iso", "IpAddress", "MibIdentifier", "TimeTicks", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "ObjectIdentity", "Counter64", "Counter32", "Bits", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
h3cDot11WLANEXT = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 7))
h3cDot11WLANEXT.setRevisions(('2007-06-08 20:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: h3cDot11WLANEXT.setRevisionsDescriptions(('The initial revision of this MIB module.',))
if mibBuilder.loadTexts: h3cDot11WLANEXT.setLastUpdated('200706082000Z')
if mibBuilder.loadTexts: h3cDot11WLANEXT.setOrganization('HUAWEI-3COM Technologies Co., Ltd.')
if mibBuilder.loadTexts: h3cDot11WLANEXT.setContactInfo('Platform Team HUAWEI-3COM Technologies Co., Ltd. Hai-Dian District Beijing P.R. China Http://www.huawei-3com.com Zip:100085')
if mibBuilder.loadTexts: h3cDot11WLANEXT.setDescription('This MIB provides more information for WLAN network. GLOSSARY IEEE 802.11 Standard to encourage interoperability among wireless networking equipment. IEEE 802.11e Standard to define the MAC procedures to support LAN applications with Quality of Service (QoS) requirements, including the transport of voice, audio and video over IEEE 802.11 wireless LANs. Access point (AP) Transmitter/receiver (transceiver) device that commonly connects and transports data between a wireless network and a wired network. Access control (AC) To control and manage multi-APs, it will bridge wireless and wired network. Radio The chip set to receive and send wireless signal. Fat AP Applied in the home, SOHO and so on, and it could independently work without help from AC. Fit AP Applied in the enterprise environment, it will work under the control and management from AC. Control And Provisioning of Wireless Access Points Protocol The short name of protocol is CAPWAP. AC will control and manage AP by CAPWAP tunnel protocol defined by IETF. Also, a data tunnel will be set up between AC and AP. Basic Service Set The IEEE 802.11 BSS of an AP comprises of the stations directly associating with the AP. It will be identified by BSSID.')
h3cDot11RFGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 7, 1))
h3cDot11QosGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 7, 2))
h3cDot11RFSignalStatisTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 7, 1, 1), )
if mibBuilder.loadTexts: h3cDot11RFSignalStatisTable.setStatus('current')
if mibBuilder.loadTexts: h3cDot11RFSignalStatisTable.setDescription('The table will describe statistic information of signal strength for AP radio.')
h3cDot11RFSignalStatisEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 7, 1, 1, 1), ).setIndexNames((0, "H3C-DOT11-WLANEXT-MIB", "h3cDot11RFAPID"), (0, "H3C-DOT11-WLANEXT-MIB", "h3cDot11RFRadioID"))
if mibBuilder.loadTexts: h3cDot11RFSignalStatisEntry.setStatus('current')
if mibBuilder.loadTexts: h3cDot11RFSignalStatisEntry.setDescription('Each entry contains the signal of each signal strength information of a specific AP.')
h3cDot11RFAPID = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 7, 1, 1, 1, 1), H3cDot11ObjectIDType())
if mibBuilder.loadTexts: h3cDot11RFAPID.setStatus('current')
if mibBuilder.loadTexts: h3cDot11RFAPID.setDescription('To identify each AP, and AP is running status.')
h3cDot11RFRadioID = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 7, 1, 1, 1, 2), H3cDot11RadioScopeType())
if mibBuilder.loadTexts: h3cDot11RFRadioID.setStatus('current')
if mibBuilder.loadTexts: h3cDot11RFRadioID.setDescription('Represents each radio.')
h3cDot11RFSignalStatisInterv = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 7, 1, 1, 1, 3), Integer32()).setUnits('second').setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11RFSignalStatisInterv.setStatus('current')
if mibBuilder.loadTexts: h3cDot11RFSignalStatisInterv.setDescription('Represents the interval of statistic.')
h3cDot11RFAverageSignalStrength = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 7, 1, 1, 1, 4), Integer32()).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11RFAverageSignalStrength.setStatus('current')
if mibBuilder.loadTexts: h3cDot11RFAverageSignalStrength.setDescription('Represents the average value of signal strength for stations on a specific radio.')
h3cDot11RFMaxSignalStrength = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 7, 1, 1, 1, 5), Integer32()).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11RFMaxSignalStrength.setStatus('current')
if mibBuilder.loadTexts: h3cDot11RFMaxSignalStrength.setDescription('Represents the maximum value of signal strength for stations on a specific radio.')
h3cDot11RFMinSignalStrength = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 7, 1, 1, 1, 6), Integer32()).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11RFMinSignalStrength.setStatus('current')
if mibBuilder.loadTexts: h3cDot11RFMinSignalStrength.setDescription('Represents the minimum value of signal strength for stations on a specific radio.')
h3cDot11QosStatisTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 7, 2, 1), )
if mibBuilder.loadTexts: h3cDot11QosStatisTable.setStatus('current')
if mibBuilder.loadTexts: h3cDot11QosStatisTable.setDescription('The table defines the attributes for the Qos feature of radio.')
h3cDot11QosStatisEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 7, 2, 1, 1), ).setIndexNames((0, "H3C-DOT11-WLANEXT-MIB", "h3cDot11QosAPID"), (0, "H3C-DOT11-WLANEXT-MIB", "h3cDot11QosRadioID"))
if mibBuilder.loadTexts: h3cDot11QosStatisEntry.setStatus('current')
if mibBuilder.loadTexts: h3cDot11QosStatisEntry.setDescription('Each entry contains information of the Qos attribute of each radio.')
h3cDot11QosAPID = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 7, 2, 1, 1, 1), H3cDot11ObjectIDType())
if mibBuilder.loadTexts: h3cDot11QosAPID.setStatus('current')
if mibBuilder.loadTexts: h3cDot11QosAPID.setDescription('To uniquely identify a AP in running status.')
h3cDot11QosRadioID = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 7, 2, 1, 1, 2), H3cDot11RadioScopeType())
if mibBuilder.loadTexts: h3cDot11QosRadioID.setStatus('current')
if mibBuilder.loadTexts: h3cDot11QosRadioID.setDescription('Represents each radio.')
h3cDot11QosAverageQueLen = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 7, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11QosAverageQueLen.setStatus('current')
if mibBuilder.loadTexts: h3cDot11QosAverageQueLen.setDescription('The average frame numbers to be sent out in the queue.')
h3cDot11QosDropFrameRatio = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 7, 2, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11QosDropFrameRatio.setStatus('current')
if mibBuilder.loadTexts: h3cDot11QosDropFrameRatio.setDescription('The ratio of dropped frames in a minute because of full queue.')
h3cDot11QosAverageDataRate = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 7, 2, 1, 1, 5), Integer32()).setUnits('Kbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11QosAverageDataRate.setStatus('current')
if mibBuilder.loadTexts: h3cDot11QosAverageDataRate.setDescription('The average transmit data rate of radio.')
h3cDot11QosAcStatisTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 7, 2, 2), )
if mibBuilder.loadTexts: h3cDot11QosAcStatisTable.setStatus('current')
if mibBuilder.loadTexts: h3cDot11QosAcStatisTable.setDescription('The table defines the parameters for Qos access category.')
h3cDot11QosAcStatisEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 7, 2, 2, 1), ).setIndexNames((0, "H3C-DOT11-WLANEXT-MIB", "h3cDot11QosAPID"), (0, "H3C-DOT11-WLANEXT-MIB", "h3cDot11QosRadioID"), (0, "H3C-DOT11-WLANEXT-MIB", "h3cDot11QosAcType"))
if mibBuilder.loadTexts: h3cDot11QosAcStatisEntry.setStatus('current')
if mibBuilder.loadTexts: h3cDot11QosAcStatisEntry.setDescription('Each entry contains information of each Qos access category.')
h3cDot11QosAcType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 7, 2, 2, 1, 1), H3cDot11QosAcType())
if mibBuilder.loadTexts: h3cDot11QosAcType.setStatus('current')
if mibBuilder.loadTexts: h3cDot11QosAcType.setDescription('The access category type.')
h3cDot11AcDropFrameCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 7, 2, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11AcDropFrameCnt.setStatus('current')
if mibBuilder.loadTexts: h3cDot11AcDropFrameCnt.setDescription('The number of dropped frames in a minute for one specific access category because of full queue.')
mibBuilder.exportSymbols("H3C-DOT11-WLANEXT-MIB", h3cDot11QosGroup=h3cDot11QosGroup, h3cDot11QosStatisEntry=h3cDot11QosStatisEntry, h3cDot11RFMaxSignalStrength=h3cDot11RFMaxSignalStrength, h3cDot11QosStatisTable=h3cDot11QosStatisTable, h3cDot11RFAPID=h3cDot11RFAPID, h3cDot11RFGroup=h3cDot11RFGroup, h3cDot11RFRadioID=h3cDot11RFRadioID, h3cDot11QosAPID=h3cDot11QosAPID, h3cDot11QosAcStatisEntry=h3cDot11QosAcStatisEntry, h3cDot11QosAcStatisTable=h3cDot11QosAcStatisTable, h3cDot11QosAverageQueLen=h3cDot11QosAverageQueLen, h3cDot11RFMinSignalStrength=h3cDot11RFMinSignalStrength, PYSNMP_MODULE_ID=h3cDot11WLANEXT, h3cDot11QosDropFrameRatio=h3cDot11QosDropFrameRatio, h3cDot11QosAverageDataRate=h3cDot11QosAverageDataRate, h3cDot11WLANEXT=h3cDot11WLANEXT, h3cDot11RFSignalStatisTable=h3cDot11RFSignalStatisTable, h3cDot11QosAcType=h3cDot11QosAcType, h3cDot11RFAverageSignalStrength=h3cDot11RFAverageSignalStrength, h3cDot11RFSignalStatisEntry=h3cDot11RFSignalStatisEntry, h3cDot11QosRadioID=h3cDot11QosRadioID, h3cDot11RFSignalStatisInterv=h3cDot11RFSignalStatisInterv, h3cDot11AcDropFrameCnt=h3cDot11AcDropFrameCnt)