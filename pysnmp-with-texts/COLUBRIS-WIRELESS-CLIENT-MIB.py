#
# PySNMP MIB module COLUBRIS-WIRELESS-CLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/COLUBRIS-WIRELESS-CLIENT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:26:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
colubrisMgmtV2, = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisMgmtV2")
systemSerialNumber, = mibBuilder.importSymbols("COLUBRIS-SYSTEM-MIB", "systemSerialNumber")
ColubrisNotificationEnable, ColubrisSSID = mibBuilder.importSymbols("COLUBRIS-TC", "ColubrisNotificationEnable", "ColubrisSSID")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
sysName, = mibBuilder.importSymbols("SNMPv2-MIB", "sysName")
ModuleIdentity, Counter32, NotificationType, MibIdentifier, Gauge32, Counter64, Bits, TimeTicks, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ObjectIdentity, iso, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter32", "NotificationType", "MibIdentifier", "Gauge32", "Counter64", "Bits", "TimeTicks", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ObjectIdentity", "iso", "Unsigned32")
TextualConvention, MacAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "MacAddress", "DisplayString")
colubrisWirelessClientMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744, 5, 20))
if mibBuilder.loadTexts: colubrisWirelessClientMIB.setLastUpdated('200610260000Z')
if mibBuilder.loadTexts: colubrisWirelessClientMIB.setOrganization('Colubris Networks, Inc.')
if mibBuilder.loadTexts: colubrisWirelessClientMIB.setContactInfo('Colubris Networks Postal: 200 West Street Ste 300 Waltham, Massachusetts 02451-1121 UNITED STATES Phone: +1 781 684 0001 Fax: +1 781 684 0009 E-mail: cn-snmp@colubris.com')
if mibBuilder.loadTexts: colubrisWirelessClientMIB.setDescription('Information for Colubris Networks client mode devices.')
colubrisWirelessClientMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 20, 1))
colubrisWirelessClientInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 1))
colubrisWirelessClientStats = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 2))
colubrisWirelessClientState = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("disconnected", 1), ("scanning", 2), ("authenticating", 3), ("associating", 4), ("associated", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: colubrisWirelessClientState.setStatus('current')
if mibBuilder.loadTexts: colubrisWirelessClientState.setDescription('802.11 status of the device.')
colubrisWirelessClientSSID = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 1, 2), ColubrisSSID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: colubrisWirelessClientSSID.setStatus('current')
if mibBuilder.loadTexts: colubrisWirelessClientSSID.setDescription('Service Set ID assigned to the device.')
colubrisWirelessClientBSSID = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: colubrisWirelessClientBSSID.setStatus('current')
if mibBuilder.loadTexts: colubrisWirelessClientBSSID.setDescription('When the client state is associated, this object identifies the MAC Address of the access point.')
colubrisWirelessClientSignalLevel = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: colubrisWirelessClientSignalLevel.setStatus('current')
if mibBuilder.loadTexts: colubrisWirelessClientSignalLevel.setDescription('Strength of the wireless signal (in dBm).')
colubrisWirelessClientNoiseLevel = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: colubrisWirelessClientNoiseLevel.setStatus('current')
if mibBuilder.loadTexts: colubrisWirelessClientNoiseLevel.setDescription('Level of local background noise (in dBm).')
colubrisWirelessClientSNR = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: colubrisWirelessClientSNR.setStatus('current')
if mibBuilder.loadTexts: colubrisWirelessClientSNR.setDescription('Relative strength of the signal level compared to the noise level.')
colubrisWirelessClientConnectionNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 1, 7), ColubrisNotificationEnable().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: colubrisWirelessClientConnectionNotificationEnabled.setStatus('current')
if mibBuilder.loadTexts: colubrisWirelessClientConnectionNotificationEnabled.setDescription('Specifies if colubrisWirelessClientConnectionNotification events are generated.')
colubrisWirelessClientConnectTime = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 1, 8), Counter32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: colubrisWirelessClientConnectTime.setStatus('current')
if mibBuilder.loadTexts: colubrisWirelessClientConnectTime.setDescription('Elapsed time in seconds since the device successfully associated with an access point.')
colubrisWirelessClientAuthorizedState = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("notAuthorized", 1), ("authorized", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: colubrisWirelessClientAuthorizedState.setStatus('current')
if mibBuilder.loadTexts: colubrisWirelessClientAuthorizedState.setDescription('Indicates if user traffic is allowed on the wireless port.')
colubrisWirelessClientEncryptionStatus = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 1), ("wep", 2), ("tkip", 3), ("aes", 4), ("aesTkip", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: colubrisWirelessClientEncryptionStatus.setStatus('current')
if mibBuilder.loadTexts: colubrisWirelessClientEncryptionStatus.setDescription('Indicates the encryption method used to communicate with the access point.')
colubrisWirelessClientTransmitRate = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: colubrisWirelessClientTransmitRate.setStatus('current')
if mibBuilder.loadTexts: colubrisWirelessClientTransmitRate.setDescription('Current data transmission rate of the station. Rates are set in increments of 500 Kb/s from 1 Mb/s to 63.5 Mb/s.')
colubrisWirelessClientReceiveRate = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: colubrisWirelessClientReceiveRate.setStatus('current')
if mibBuilder.loadTexts: colubrisWirelessClientReceiveRate.setDescription('Current receive rate of the station. Rates are set in increments of 500 Kb/s from 1 Mb/s to 63.5 Mb/s.')
colubrisWirelessClientInPkts = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 2, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: colubrisWirelessClientInPkts.setStatus('current')
if mibBuilder.loadTexts: colubrisWirelessClientInPkts.setDescription('Number of packets received since associating with an access point.')
colubrisWirelessClientOutPkts = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 2, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: colubrisWirelessClientOutPkts.setStatus('current')
if mibBuilder.loadTexts: colubrisWirelessClientOutPkts.setDescription('Number of packets sent since associating with an access point.')
colubrisWirelessClientInOctets = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 2, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: colubrisWirelessClientInOctets.setStatus('current')
if mibBuilder.loadTexts: colubrisWirelessClientInOctets.setDescription('Number of octets received since associating with an access point.')
colubrisWirelessClientOutOctets = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 2, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: colubrisWirelessClientOutOctets.setStatus('current')
if mibBuilder.loadTexts: colubrisWirelessClientOutOctets.setDescription('Number of octets sent since associating with an access point.')
colubrisWirelessClientPktsTxRate1 = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 2, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: colubrisWirelessClientPktsTxRate1.setStatus('current')
if mibBuilder.loadTexts: colubrisWirelessClientPktsTxRate1.setDescription('Number of frames transmitted at 1 Mbit/s since associating with an access point.')
colubrisWirelessClientPktsTxRate2 = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 2, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: colubrisWirelessClientPktsTxRate2.setStatus('current')
if mibBuilder.loadTexts: colubrisWirelessClientPktsTxRate2.setDescription('Number of frames transmitted at 2 Mbit/s since associating with an access point.')
colubrisWirelessClientPktsTxRate5dot5 = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 2, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: colubrisWirelessClientPktsTxRate5dot5.setStatus('current')
if mibBuilder.loadTexts: colubrisWirelessClientPktsTxRate5dot5.setDescription('Number of frames transmitted at 5.5 Mbit/s since associating with an access point.')
colubrisWirelessClientPktsTxRate11 = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 2, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: colubrisWirelessClientPktsTxRate11.setStatus('current')
if mibBuilder.loadTexts: colubrisWirelessClientPktsTxRate11.setDescription('Number of frames transmitted at 11 Mbit/s since associating with an access point.')
colubrisWirelessClientPktsTxRate6 = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 2, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: colubrisWirelessClientPktsTxRate6.setStatus('current')
if mibBuilder.loadTexts: colubrisWirelessClientPktsTxRate6.setDescription('Number of frames transmitted at 6 Mbit/s since associating with an access point.')
colubrisWirelessClientPktsTxRate9 = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 2, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: colubrisWirelessClientPktsTxRate9.setStatus('current')
if mibBuilder.loadTexts: colubrisWirelessClientPktsTxRate9.setDescription('Number of frames transmitted at 9 Mbit/s since associating with an access point.')
colubrisWirelessClientPktsTxRate12 = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 2, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: colubrisWirelessClientPktsTxRate12.setStatus('current')
if mibBuilder.loadTexts: colubrisWirelessClientPktsTxRate12.setDescription('Number of frames transmitted at 12 Mbit/s since associating with an access point.')
colubrisWirelessClientPktsTxRate18 = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 2, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: colubrisWirelessClientPktsTxRate18.setStatus('current')
if mibBuilder.loadTexts: colubrisWirelessClientPktsTxRate18.setDescription('Number of frames transmitted at 18 Mbit/s since associating with an access point.')
colubrisWirelessClientPktsTxRate24 = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 2, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: colubrisWirelessClientPktsTxRate24.setStatus('current')
if mibBuilder.loadTexts: colubrisWirelessClientPktsTxRate24.setDescription('Number of frames transmitted at 24 Mbit/s since associating with an access point.')
colubrisWirelessClientPktsTxRate36 = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 2, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: colubrisWirelessClientPktsTxRate36.setStatus('current')
if mibBuilder.loadTexts: colubrisWirelessClientPktsTxRate36.setDescription('Number of frames transmitted at 36 Mbit/s since associating with an access point.')
colubrisWirelessClientPktsTxRate48 = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 2, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: colubrisWirelessClientPktsTxRate48.setStatus('current')
if mibBuilder.loadTexts: colubrisWirelessClientPktsTxRate48.setDescription('Number of frames transmitted at 48 Mbit/s since associating with an access point.')
colubrisWirelessClientPktsTxRate54 = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 2, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: colubrisWirelessClientPktsTxRate54.setStatus('current')
if mibBuilder.loadTexts: colubrisWirelessClientPktsTxRate54.setDescription('Number of frames transmitted at 54 Mbit/s since associating with an access point.')
colubrisWirelessClientPktsRxRate1 = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 2, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: colubrisWirelessClientPktsRxRate1.setStatus('current')
if mibBuilder.loadTexts: colubrisWirelessClientPktsRxRate1.setDescription('Number of frames received at 1 Mbit/s since associating with an access point.')
colubrisWirelessClientPktsRxRate2 = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 2, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: colubrisWirelessClientPktsRxRate2.setStatus('current')
if mibBuilder.loadTexts: colubrisWirelessClientPktsRxRate2.setDescription('Number of frames received at 2 Mbit/s since associating with an access point.')
colubrisWirelessClientPktsRxRate5dot5 = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 2, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: colubrisWirelessClientPktsRxRate5dot5.setStatus('current')
if mibBuilder.loadTexts: colubrisWirelessClientPktsRxRate5dot5.setDescription('Number of frames received at 5.5 Mbit/s since associating with an access point.')
colubrisWirelessClientPktsRxRate11 = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 2, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: colubrisWirelessClientPktsRxRate11.setStatus('current')
if mibBuilder.loadTexts: colubrisWirelessClientPktsRxRate11.setDescription('Number of frames received at 11 Mbit/s since associating with an access point.')
colubrisWirelessClientPktsRxRate6 = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 2, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: colubrisWirelessClientPktsRxRate6.setStatus('current')
if mibBuilder.loadTexts: colubrisWirelessClientPktsRxRate6.setDescription('Number of frames received at 6 Mbit/s since associating with an access point.')
colubrisWirelessClientPktsRxRate9 = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 2, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: colubrisWirelessClientPktsRxRate9.setStatus('current')
if mibBuilder.loadTexts: colubrisWirelessClientPktsRxRate9.setDescription('Number of frames received at 9 Mbit/s since associating with an access point.')
colubrisWirelessClientPktsRxRate12 = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 2, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: colubrisWirelessClientPktsRxRate12.setStatus('current')
if mibBuilder.loadTexts: colubrisWirelessClientPktsRxRate12.setDescription('Number of frames received at 12 Mbit/s since associating with an access point.')
colubrisWirelessClientPktsRxRate18 = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 2, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: colubrisWirelessClientPktsRxRate18.setStatus('current')
if mibBuilder.loadTexts: colubrisWirelessClientPktsRxRate18.setDescription('Number of frames received at 18 Mbit/s since associating with an access point.')
colubrisWirelessClientPktsRxRate24 = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 2, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: colubrisWirelessClientPktsRxRate24.setStatus('current')
if mibBuilder.loadTexts: colubrisWirelessClientPktsRxRate24.setDescription('Number of frames received at 24 Mbit/s since associating with an access point.')
colubrisWirelessClientPktsRxRate36 = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 2, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: colubrisWirelessClientPktsRxRate36.setStatus('current')
if mibBuilder.loadTexts: colubrisWirelessClientPktsRxRate36.setDescription('Number of frames received at 36 Mbit/s since associating with an access point.')
colubrisWirelessClientPktsRxRate48 = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 2, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: colubrisWirelessClientPktsRxRate48.setStatus('current')
if mibBuilder.loadTexts: colubrisWirelessClientPktsRxRate48.setDescription('Number of frames received at 48 Mbit/s since associating with an access point.')
colubrisWirelessClientPktsRxRate54 = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 2, 28), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: colubrisWirelessClientPktsRxRate54.setStatus('current')
if mibBuilder.loadTexts: colubrisWirelessClientPktsRxRate54.setDescription('Number of frames received at 54 Mbit/s since associating with an access point.')
colubrisWirelessClientMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 20, 2))
colubrisWirelessClientMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 20, 2, 0))
colubrisWirelessClientConnectionNotification = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 20, 2, 0, 1)).setObjects(("SNMPv2-MIB", "sysName"), ("COLUBRIS-SYSTEM-MIB", "systemSerialNumber"), ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientSSID"), ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientBSSID"))
if mibBuilder.loadTexts: colubrisWirelessClientConnectionNotification.setStatus('current')
if mibBuilder.loadTexts: colubrisWirelessClientConnectionNotification.setDescription('Sent when an 802.11/802.1X connection is successfully completed.')
colubrisWirelessClientMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 20, 3))
colubrisWirelessClientMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 20, 3, 1))
colubrisWirelessClientMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 20, 3, 2))
colubrisWirelessClientMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 8744, 5, 20, 3, 1, 1)).setObjects(("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientMIBGroup"), ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientNotificationGroup"), ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientMIBGroupCounters"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisWirelessClientMIBCompliance = colubrisWirelessClientMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: colubrisWirelessClientMIBCompliance.setDescription('The compliance statement for entities which implement the wireless client extensions MIB.')
colubrisWirelessClientMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 20, 3, 2, 1)).setObjects(("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientState"), ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientSSID"), ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientBSSID"), ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientSignalLevel"), ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientNoiseLevel"), ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientSNR"), ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientConnectionNotificationEnabled"), ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientTransmitRate"), ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientReceiveRate"), ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientConnectTime"), ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientAuthorizedState"), ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientEncryptionStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisWirelessClientMIBGroup = colubrisWirelessClientMIBGroup.setStatus('current')
if mibBuilder.loadTexts: colubrisWirelessClientMIBGroup.setDescription('A collection of objects providing the Client MIB capability.')
colubrisWirelessClientNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 8744, 5, 20, 3, 2, 2)).setObjects(("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientConnectionNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisWirelessClientNotificationGroup = colubrisWirelessClientNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: colubrisWirelessClientNotificationGroup.setDescription('A collection of supported notifications.')
colubrisWirelessClientMIBGroupCounters = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 20, 3, 2, 3)).setObjects(("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientInPkts"), ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientOutPkts"), ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientInOctets"), ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientOutOctets"), ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientPktsTxRate1"), ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientPktsTxRate2"), ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientPktsTxRate5dot5"), ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientPktsTxRate11"), ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientPktsTxRate6"), ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientPktsTxRate9"), ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientPktsTxRate12"), ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientPktsTxRate18"), ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientPktsTxRate24"), ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientPktsTxRate36"), ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientPktsTxRate48"), ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientPktsTxRate54"), ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientPktsRxRate1"), ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientPktsRxRate2"), ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientPktsRxRate5dot5"), ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientPktsRxRate11"), ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientPktsRxRate6"), ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientPktsRxRate9"), ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientPktsRxRate12"), ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientPktsRxRate18"), ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientPktsRxRate24"), ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientPktsRxRate36"), ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientPktsRxRate48"), ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientPktsRxRate54"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisWirelessClientMIBGroupCounters = colubrisWirelessClientMIBGroupCounters.setStatus('current')
if mibBuilder.loadTexts: colubrisWirelessClientMIBGroupCounters.setDescription('A collection of objects providing the Client MIB counters.')
mibBuilder.exportSymbols("COLUBRIS-WIRELESS-CLIENT-MIB", colubrisWirelessClientMIBGroups=colubrisWirelessClientMIBGroups, colubrisWirelessClientInPkts=colubrisWirelessClientInPkts, colubrisWirelessClientEncryptionStatus=colubrisWirelessClientEncryptionStatus, colubrisWirelessClientPktsRxRate18=colubrisWirelessClientPktsRxRate18, colubrisWirelessClientMIBNotifications=colubrisWirelessClientMIBNotifications, colubrisWirelessClientPktsTxRate18=colubrisWirelessClientPktsTxRate18, colubrisWirelessClientPktsTxRate6=colubrisWirelessClientPktsTxRate6, colubrisWirelessClientPktsTxRate54=colubrisWirelessClientPktsTxRate54, PYSNMP_MODULE_ID=colubrisWirelessClientMIB, colubrisWirelessClientSSID=colubrisWirelessClientSSID, colubrisWirelessClientPktsRxRate5dot5=colubrisWirelessClientPktsRxRate5dot5, colubrisWirelessClientPktsRxRate54=colubrisWirelessClientPktsRxRate54, colubrisWirelessClientPktsTxRate9=colubrisWirelessClientPktsTxRate9, colubrisWirelessClientMIBGroup=colubrisWirelessClientMIBGroup, colubrisWirelessClientPktsRxRate2=colubrisWirelessClientPktsRxRate2, colubrisWirelessClientMIBCompliances=colubrisWirelessClientMIBCompliances, colubrisWirelessClientInOctets=colubrisWirelessClientInOctets, colubrisWirelessClientMIBNotificationPrefix=colubrisWirelessClientMIBNotificationPrefix, colubrisWirelessClientNotificationGroup=colubrisWirelessClientNotificationGroup, colubrisWirelessClientMIBConformance=colubrisWirelessClientMIBConformance, colubrisWirelessClientPktsRxRate36=colubrisWirelessClientPktsRxRate36, colubrisWirelessClientSNR=colubrisWirelessClientSNR, colubrisWirelessClientOutOctets=colubrisWirelessClientOutOctets, colubrisWirelessClientPktsTxRate48=colubrisWirelessClientPktsTxRate48, colubrisWirelessClientConnectionNotificationEnabled=colubrisWirelessClientConnectionNotificationEnabled, colubrisWirelessClientState=colubrisWirelessClientState, colubrisWirelessClientMIBObjects=colubrisWirelessClientMIBObjects, colubrisWirelessClientMIB=colubrisWirelessClientMIB, colubrisWirelessClientBSSID=colubrisWirelessClientBSSID, colubrisWirelessClientPktsTxRate24=colubrisWirelessClientPktsTxRate24, colubrisWirelessClientTransmitRate=colubrisWirelessClientTransmitRate, colubrisWirelessClientPktsTxRate36=colubrisWirelessClientPktsTxRate36, colubrisWirelessClientMIBCompliance=colubrisWirelessClientMIBCompliance, colubrisWirelessClientInfo=colubrisWirelessClientInfo, colubrisWirelessClientPktsRxRate24=colubrisWirelessClientPktsRxRate24, colubrisWirelessClientPktsRxRate12=colubrisWirelessClientPktsRxRate12, colubrisWirelessClientStats=colubrisWirelessClientStats, colubrisWirelessClientPktsTxRate5dot5=colubrisWirelessClientPktsTxRate5dot5, colubrisWirelessClientNoiseLevel=colubrisWirelessClientNoiseLevel, colubrisWirelessClientPktsTxRate2=colubrisWirelessClientPktsTxRate2, colubrisWirelessClientPktsRxRate11=colubrisWirelessClientPktsRxRate11, colubrisWirelessClientOutPkts=colubrisWirelessClientOutPkts, colubrisWirelessClientPktsRxRate48=colubrisWirelessClientPktsRxRate48, colubrisWirelessClientMIBGroupCounters=colubrisWirelessClientMIBGroupCounters, colubrisWirelessClientSignalLevel=colubrisWirelessClientSignalLevel, colubrisWirelessClientReceiveRate=colubrisWirelessClientReceiveRate, colubrisWirelessClientConnectTime=colubrisWirelessClientConnectTime, colubrisWirelessClientPktsTxRate11=colubrisWirelessClientPktsTxRate11, colubrisWirelessClientPktsRxRate1=colubrisWirelessClientPktsRxRate1, colubrisWirelessClientPktsTxRate1=colubrisWirelessClientPktsTxRate1, colubrisWirelessClientConnectionNotification=colubrisWirelessClientConnectionNotification, colubrisWirelessClientPktsRxRate9=colubrisWirelessClientPktsRxRate9, colubrisWirelessClientAuthorizedState=colubrisWirelessClientAuthorizedState, colubrisWirelessClientPktsRxRate6=colubrisWirelessClientPktsRxRate6, colubrisWirelessClientPktsTxRate12=colubrisWirelessClientPktsTxRate12)
