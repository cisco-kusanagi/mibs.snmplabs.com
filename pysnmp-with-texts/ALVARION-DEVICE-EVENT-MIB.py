#
# PySNMP MIB module ALVARION-DEVICE-EVENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALVARION-DEVICE-EVENT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:22:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
coDevDisIndex, = mibBuilder.importSymbols("ALVARION-DEVICE-MIB", "coDevDisIndex")
alvarionMgmtV2, = mibBuilder.importSymbols("ALVARION-SMI", "alvarionMgmtV2")
AlvarionNotificationEnable, AlvarionSSIDOrNone = mibBuilder.importSymbols("ALVARION-TC", "AlvarionNotificationEnable", "AlvarionSSIDOrNone")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
TimeTicks, ObjectIdentity, ModuleIdentity, NotificationType, Gauge32, MibIdentifier, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32, Integer32, Counter64, IpAddress, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ObjectIdentity", "ModuleIdentity", "NotificationType", "Gauge32", "MibIdentifier", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32", "Integer32", "Counter64", "IpAddress", "Counter32")
DisplayString, TextualConvention, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "MacAddress")
alvarionDeviceEventMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26))
if mibBuilder.loadTexts: alvarionDeviceEventMIB.setLastUpdated('200710310000Z')
if mibBuilder.loadTexts: alvarionDeviceEventMIB.setOrganization('Alvarion Ltd.')
if mibBuilder.loadTexts: alvarionDeviceEventMIB.setContactInfo('Alvarion Ltd. Postal: 21a HaBarzel St. P.O. Box 13139 Tel-Aviv 69710 Israel Phone: +972 3 645 6262')
if mibBuilder.loadTexts: alvarionDeviceEventMIB.setDescription('Alvarion Device Event MIB.')
alvarionDeviceEventMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1))
coDeviceEventConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 1))
coDeviceEventInfoGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 2))
coDevEvSuccessfulAssociationNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 1, 1), AlvarionNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDevEvSuccessfulAssociationNotificationEnabled.setStatus('current')
if mibBuilder.loadTexts: coDevEvSuccessfulAssociationNotificationEnabled.setDescription('Specifies if coDeviceEventSuccessfulAssociation notifications are generated.')
coDevEvAssociationFailureNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 1, 2), AlvarionNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDevEvAssociationFailureNotificationEnabled.setStatus('current')
if mibBuilder.loadTexts: coDevEvAssociationFailureNotificationEnabled.setDescription('Specifies if coDeviceEventAssociationFailure notifications are generated.')
coDevEvSuccessfulReAssociationNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 1, 3), AlvarionNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDevEvSuccessfulReAssociationNotificationEnabled.setStatus('current')
if mibBuilder.loadTexts: coDevEvSuccessfulReAssociationNotificationEnabled.setDescription('Specifies if coDeviceEventSuccessfulReAssociation notifications are generated.')
coDevEvReAssociationFailureNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 1, 4), AlvarionNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDevEvReAssociationFailureNotificationEnabled.setStatus('current')
if mibBuilder.loadTexts: coDevEvReAssociationFailureNotificationEnabled.setDescription('Specifies if coDeviceEventReAssociationFailure notifications are generated.')
coDevEvSuccessfulAuthenticationNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 1, 5), AlvarionNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDevEvSuccessfulAuthenticationNotificationEnabled.setStatus('current')
if mibBuilder.loadTexts: coDevEvSuccessfulAuthenticationNotificationEnabled.setDescription('Specifies if coDeviceEventSuccessfulAuthentication notifications are generated.')
coDevEvAuthenticationFailureNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 1, 6), AlvarionNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDevEvAuthenticationFailureNotificationEnabled.setStatus('current')
if mibBuilder.loadTexts: coDevEvAuthenticationFailureNotificationEnabled.setDescription('Specifies if coDeviceEventAuthenticationFailure notifications are generated.')
coDevEvSuccessfulDisAssociationNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 1, 7), AlvarionNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDevEvSuccessfulDisAssociationNotificationEnabled.setStatus('current')
if mibBuilder.loadTexts: coDevEvSuccessfulDisAssociationNotificationEnabled.setDescription('Specifies if coDeviceEventSuccessfulDisAssociation notifications are generated.')
coDevEvDisAssociationFailureNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 1, 8), AlvarionNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDevEvDisAssociationFailureNotificationEnabled.setStatus('current')
if mibBuilder.loadTexts: coDevEvDisAssociationFailureNotificationEnabled.setDescription('Specifies if coDeviceEventDisAssociationFailure notifications are generated.')
coDevEvSuccessfulDeAuthenticationNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 1, 9), AlvarionNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDevEvSuccessfulDeAuthenticationNotificationEnabled.setStatus('current')
if mibBuilder.loadTexts: coDevEvSuccessfulDeAuthenticationNotificationEnabled.setDescription('Specifies if coDeviceEventSuccessfulDeAuthentication notifications are generated.')
coDevEvDeAuthenticationFailureNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 1, 10), AlvarionNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDevEvDeAuthenticationFailureNotificationEnabled.setStatus('current')
if mibBuilder.loadTexts: coDevEvDeAuthenticationFailureNotificationEnabled.setDescription('Specifies if coDeviceEventDeAuthenticationFailure notifications are generated.')
coDeviceEventTable = MibTable((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 2, 1), )
if mibBuilder.loadTexts: coDeviceEventTable.setStatus('current')
if mibBuilder.loadTexts: coDeviceEventTable.setDescription('The list of devices available in the Event system.')
coDeviceEventEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 2, 1, 1), ).setIndexNames((0, "ALVARION-DEVICE-MIB", "coDevDisIndex"), (0, "ALVARION-DEVICE-EVENT-MIB", "coDevEvIndex"))
if mibBuilder.loadTexts: coDeviceEventEntry.setStatus('current')
if mibBuilder.loadTexts: coDeviceEventEntry.setDescription('An entry in the coDeviceEventTable. coDevDisIndex - Uniquely identify a device in the MultiService Access Controller. coDevEvIndex - Uniquely identify a device in the Event system.')
coDevEvIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: coDevEvIndex.setStatus('current')
if mibBuilder.loadTexts: coDevEvIndex.setDescription('Specifies the index associated to a device in the Event system.')
coDevEvMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 2, 1, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevEvMacAddress.setStatus('current')
if mibBuilder.loadTexts: coDevEvMacAddress.setDescription("MAC address of the device's generating the events.")
coDeviceEventDetailTable = MibTable((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 2, 2), )
if mibBuilder.loadTexts: coDeviceEventDetailTable.setStatus('current')
if mibBuilder.loadTexts: coDeviceEventDetailTable.setDescription('The Event for each devices.')
coDeviceEventDetailEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 2, 2, 1), ).setIndexNames((0, "ALVARION-DEVICE-MIB", "coDevDisIndex"), (0, "ALVARION-DEVICE-EVENT-MIB", "coDevEvIndex"), (0, "ALVARION-DEVICE-EVENT-MIB", "coDevEvLogIndex"))
if mibBuilder.loadTexts: coDeviceEventDetailEntry.setStatus('current')
if mibBuilder.loadTexts: coDeviceEventDetailEntry.setDescription('An entry in the coDeviceEventDetailTable. coDevDisIndex - Uniquely identifies a device on the MultiService Access Controller. coDevEvIndex - Uniquely identifies a device on the Event system. coDevEvLogIndex - Uniquely identifies a log for a specific device in the Event system. ')
coDevEvLogIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: coDevEvLogIndex.setStatus('current')
if mibBuilder.loadTexts: coDevEvLogIndex.setDescription('Uniquely identifies a log for a specific device in the Event system.')
coDevEvDetMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 2, 2, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevEvDetMacAddress.setStatus('current')
if mibBuilder.loadTexts: coDevEvDetMacAddress.setDescription('MAC address of the device generating the events.')
coDevEvTime = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 2, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevEvTime.setStatus('current')
if mibBuilder.loadTexts: coDevEvTime.setDescription('Date and time of the event.')
coDevEvSSID = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 2, 2, 1, 4), AlvarionSSIDOrNone()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevEvSSID.setStatus('current')
if mibBuilder.loadTexts: coDevEvSSID.setDescription('The SSID used by the wireless device.')
coDevEvRadioIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevEvRadioIndex.setStatus('current')
if mibBuilder.loadTexts: coDevEvRadioIndex.setDescription('Radio index where the wireless device is connected.')
coDevEvDuplicateCount = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 2, 2, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevEvDuplicateCount.setStatus('current')
if mibBuilder.loadTexts: coDevEvDuplicateCount.setDescription('Number of times this event is repeated.')
coDevEvCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 2, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("wireless", 1), ("ieee802dot1x", 2), ("wpa", 3), ("macAuthentication", 4), ("dhcpServer", 5), ("pptpL2tp", 6), ("ipSec", 7), ("unknown", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevEvCategory.setStatus('current')
if mibBuilder.loadTexts: coDevEvCategory.setDescription('The module that sent the message.')
coDevEvOperation = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 2, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("association", 1), ("authentication", 2), ("authorization", 3), ("encryption", 4), ("addressAllocation", 5), ("vpnAuthentication", 6), ("vpnAddressAllocation", 7), ("unknown", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevEvOperation.setStatus('current')
if mibBuilder.loadTexts: coDevEvOperation.setDescription('The action that has occured.')
coDevEvStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 2, 2, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevEvStatus.setStatus('current')
if mibBuilder.loadTexts: coDevEvStatus.setDescription('The status itself.')
coDevEvOptionalData = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 2, 2, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevEvOptionalData.setStatus('current')
if mibBuilder.loadTexts: coDevEvOptionalData.setDescription('Additional data that may be supplied (reason codes, etc).')
alvarionDeviceEventMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 2))
alvarionDeviceEventMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 2, 0))
coDeviceEventSuccessfulAssociation = NotificationType((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 2, 0, 1)).setObjects(("ALVARION-DEVICE-EVENT-MIB", "coDevEvMacAddress"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvSSID"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvStatus"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvOptionalData"))
if mibBuilder.loadTexts: coDeviceEventSuccessfulAssociation.setStatus('current')
if mibBuilder.loadTexts: coDeviceEventSuccessfulAssociation.setDescription('Sent when a client station is successfully associated with the AP.')
coDeviceEventAssociationFailure = NotificationType((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 2, 0, 2)).setObjects(("ALVARION-DEVICE-EVENT-MIB", "coDevEvMacAddress"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvSSID"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvStatus"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvOptionalData"))
if mibBuilder.loadTexts: coDeviceEventAssociationFailure.setStatus('current')
if mibBuilder.loadTexts: coDeviceEventAssociationFailure.setDescription('Sent when a client station has failed to associate with the AP.')
coDeviceEventSuccessfulReAssociation = NotificationType((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 2, 0, 3)).setObjects(("ALVARION-DEVICE-EVENT-MIB", "coDevEvMacAddress"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvSSID"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvStatus"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvOptionalData"))
if mibBuilder.loadTexts: coDeviceEventSuccessfulReAssociation.setStatus('current')
if mibBuilder.loadTexts: coDeviceEventSuccessfulReAssociation.setDescription('Sent when a client station is successfully reassociated with the AP.')
coDeviceEventReAssociationFailure = NotificationType((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 2, 0, 4)).setObjects(("ALVARION-DEVICE-EVENT-MIB", "coDevEvMacAddress"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvSSID"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvStatus"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvOptionalData"))
if mibBuilder.loadTexts: coDeviceEventReAssociationFailure.setStatus('current')
if mibBuilder.loadTexts: coDeviceEventReAssociationFailure.setDescription('Sent when a client station has failed to reassociate with the AP.')
coDeviceEventSuccessfulAuthentication = NotificationType((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 2, 0, 5)).setObjects(("ALVARION-DEVICE-EVENT-MIB", "coDevEvMacAddress"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvSSID"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvStatus"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvOptionalData"))
if mibBuilder.loadTexts: coDeviceEventSuccessfulAuthentication.setStatus('current')
if mibBuilder.loadTexts: coDeviceEventSuccessfulAuthentication.setDescription('Sent when a client station is successfully authenticated.')
coDeviceEventAuthenticationFailure = NotificationType((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 2, 0, 6)).setObjects(("ALVARION-DEVICE-EVENT-MIB", "coDevEvMacAddress"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvSSID"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvStatus"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvOptionalData"))
if mibBuilder.loadTexts: coDeviceEventAuthenticationFailure.setStatus('current')
if mibBuilder.loadTexts: coDeviceEventAuthenticationFailure.setDescription('Sent when a client station has failed to authenticate.')
coDeviceEventSuccessfulDisAssociation = NotificationType((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 2, 0, 7)).setObjects(("ALVARION-DEVICE-EVENT-MIB", "coDevEvMacAddress"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvSSID"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvStatus"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvOptionalData"))
if mibBuilder.loadTexts: coDeviceEventSuccessfulDisAssociation.setStatus('current')
if mibBuilder.loadTexts: coDeviceEventSuccessfulDisAssociation.setDescription('Sent when a client station is successfully disassociated from the AP.')
coDeviceEventDisAssociationFailure = NotificationType((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 2, 0, 8)).setObjects(("ALVARION-DEVICE-EVENT-MIB", "coDevEvMacAddress"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvSSID"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvStatus"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvOptionalData"))
if mibBuilder.loadTexts: coDeviceEventDisAssociationFailure.setStatus('current')
if mibBuilder.loadTexts: coDeviceEventDisAssociationFailure.setDescription('Sent when a client station has failed to disassociate from the AP.')
coDeviceEventSuccessfulDeAuthentication = NotificationType((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 2, 0, 9)).setObjects(("ALVARION-DEVICE-EVENT-MIB", "coDevEvMacAddress"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvSSID"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvStatus"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvOptionalData"))
if mibBuilder.loadTexts: coDeviceEventSuccessfulDeAuthentication.setStatus('current')
if mibBuilder.loadTexts: coDeviceEventSuccessfulDeAuthentication.setDescription('Sent when a client station is successfully deauthenticated.')
coDeviceEventDeAuthenticationFailure = NotificationType((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 2, 0, 10)).setObjects(("ALVARION-DEVICE-EVENT-MIB", "coDevEvMacAddress"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvSSID"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvStatus"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvOptionalData"))
if mibBuilder.loadTexts: coDeviceEventDeAuthenticationFailure.setStatus('current')
if mibBuilder.loadTexts: coDeviceEventDeAuthenticationFailure.setDescription('Sent when a client station has failed to deauthenticate.')
alvarionDeviceEventMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 3))
alvarionDeviceEventMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 3, 1))
alvarionDeviceEventMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 3, 2))
alvarionDeviceEventMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 3, 1, 1)).setObjects(("ALVARION-DEVICE-EVENT-MIB", "alvarionDeviceEventConfigMIBGroup"), ("ALVARION-DEVICE-EVENT-MIB", "alvarionDeviceEventInfoMIBGroup"), ("ALVARION-DEVICE-EVENT-MIB", "alvarionDeviceEventNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionDeviceEventMIBCompliance = alvarionDeviceEventMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: alvarionDeviceEventMIBCompliance.setDescription('The compliance statement for the Event Log MIB.')
alvarionDeviceEventConfigMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 3, 2, 1)).setObjects(("ALVARION-DEVICE-EVENT-MIB", "coDevEvSuccessfulAssociationNotificationEnabled"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvAssociationFailureNotificationEnabled"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvSuccessfulReAssociationNotificationEnabled"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvReAssociationFailureNotificationEnabled"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvSuccessfulAuthenticationNotificationEnabled"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvAuthenticationFailureNotificationEnabled"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvSuccessfulDisAssociationNotificationEnabled"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvDisAssociationFailureNotificationEnabled"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvSuccessfulDeAuthenticationNotificationEnabled"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvDeAuthenticationFailureNotificationEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionDeviceEventConfigMIBGroup = alvarionDeviceEventConfigMIBGroup.setStatus('current')
if mibBuilder.loadTexts: alvarionDeviceEventConfigMIBGroup.setDescription('A collection of objects for Device Event configuration.')
alvarionDeviceEventInfoMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 3, 2, 2)).setObjects(("ALVARION-DEVICE-EVENT-MIB", "coDevEvMacAddress"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvDetMacAddress"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvTime"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvSSID"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvRadioIndex"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvDuplicateCount"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvCategory"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvOperation"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvStatus"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvOptionalData"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionDeviceEventInfoMIBGroup = alvarionDeviceEventInfoMIBGroup.setStatus('current')
if mibBuilder.loadTexts: alvarionDeviceEventInfoMIBGroup.setDescription('A collection of objects for Device Event status.')
alvarionDeviceEventNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 3, 2, 3)).setObjects(("ALVARION-DEVICE-EVENT-MIB", "coDeviceEventSuccessfulAssociation"), ("ALVARION-DEVICE-EVENT-MIB", "coDeviceEventAssociationFailure"), ("ALVARION-DEVICE-EVENT-MIB", "coDeviceEventSuccessfulReAssociation"), ("ALVARION-DEVICE-EVENT-MIB", "coDeviceEventReAssociationFailure"), ("ALVARION-DEVICE-EVENT-MIB", "coDeviceEventSuccessfulAuthentication"), ("ALVARION-DEVICE-EVENT-MIB", "coDeviceEventAuthenticationFailure"), ("ALVARION-DEVICE-EVENT-MIB", "coDeviceEventSuccessfulDisAssociation"), ("ALVARION-DEVICE-EVENT-MIB", "coDeviceEventDisAssociationFailure"), ("ALVARION-DEVICE-EVENT-MIB", "coDeviceEventSuccessfulDeAuthentication"), ("ALVARION-DEVICE-EVENT-MIB", "coDeviceEventDeAuthenticationFailure"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionDeviceEventNotificationGroup = alvarionDeviceEventNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: alvarionDeviceEventNotificationGroup.setDescription('A collection of supported Device Event notifications.')
mibBuilder.exportSymbols("ALVARION-DEVICE-EVENT-MIB", coDeviceEventSuccessfulReAssociation=coDeviceEventSuccessfulReAssociation, coDevEvReAssociationFailureNotificationEnabled=coDevEvReAssociationFailureNotificationEnabled, coDevEvSuccessfulDeAuthenticationNotificationEnabled=coDevEvSuccessfulDeAuthenticationNotificationEnabled, alvarionDeviceEventInfoMIBGroup=alvarionDeviceEventInfoMIBGroup, coDevEvSuccessfulAuthenticationNotificationEnabled=coDevEvSuccessfulAuthenticationNotificationEnabled, coDevEvLogIndex=coDevEvLogIndex, coDevEvSuccessfulAssociationNotificationEnabled=coDevEvSuccessfulAssociationNotificationEnabled, alvarionDeviceEventMIBNotificationPrefix=alvarionDeviceEventMIBNotificationPrefix, coDeviceEventDetailTable=coDeviceEventDetailTable, alvarionDeviceEventMIB=alvarionDeviceEventMIB, coDeviceEventAuthenticationFailure=coDeviceEventAuthenticationFailure, coDeviceEventDisAssociationFailure=coDeviceEventDisAssociationFailure, coDeviceEventSuccessfulDisAssociation=coDeviceEventSuccessfulDisAssociation, coDevEvMacAddress=coDevEvMacAddress, coDeviceEventSuccessfulAssociation=coDeviceEventSuccessfulAssociation, coDevEvSuccessfulDisAssociationNotificationEnabled=coDevEvSuccessfulDisAssociationNotificationEnabled, coDeviceEventInfoGroup=coDeviceEventInfoGroup, alvarionDeviceEventMIBConformance=alvarionDeviceEventMIBConformance, alvarionDeviceEventMIBCompliance=alvarionDeviceEventMIBCompliance, coDevEvDisAssociationFailureNotificationEnabled=coDevEvDisAssociationFailureNotificationEnabled, coDevEvDeAuthenticationFailureNotificationEnabled=coDevEvDeAuthenticationFailureNotificationEnabled, coDevEvCategory=coDevEvCategory, coDevEvIndex=coDevEvIndex, coDeviceEventTable=coDeviceEventTable, coDevEvStatus=coDevEvStatus, coDeviceEventDetailEntry=coDeviceEventDetailEntry, coDeviceEventSuccessfulAuthentication=coDeviceEventSuccessfulAuthentication, coDevEvAssociationFailureNotificationEnabled=coDevEvAssociationFailureNotificationEnabled, coDevEvSuccessfulReAssociationNotificationEnabled=coDevEvSuccessfulReAssociationNotificationEnabled, coDevEvRadioIndex=coDevEvRadioIndex, coDevEvDuplicateCount=coDevEvDuplicateCount, alvarionDeviceEventConfigMIBGroup=alvarionDeviceEventConfigMIBGroup, coDeviceEventReAssociationFailure=coDeviceEventReAssociationFailure, coDeviceEventDeAuthenticationFailure=coDeviceEventDeAuthenticationFailure, alvarionDeviceEventMIBCompliances=alvarionDeviceEventMIBCompliances, coDevEvOperation=coDevEvOperation, coDevEvSSID=coDevEvSSID, coDevEvOptionalData=coDevEvOptionalData, PYSNMP_MODULE_ID=alvarionDeviceEventMIB, coDeviceEventConfigGroup=coDeviceEventConfigGroup, alvarionDeviceEventMIBGroups=alvarionDeviceEventMIBGroups, coDevEvAuthenticationFailureNotificationEnabled=coDevEvAuthenticationFailureNotificationEnabled, alvarionDeviceEventMIBNotifications=alvarionDeviceEventMIBNotifications, coDeviceEventSuccessfulDeAuthentication=coDeviceEventSuccessfulDeAuthentication, coDeviceEventAssociationFailure=coDeviceEventAssociationFailure, coDeviceEventEntry=coDeviceEventEntry, alvarionDeviceEventMIBObjects=alvarionDeviceEventMIBObjects, coDevEvTime=coDevEvTime, coDevEvDetMacAddress=coDevEvDetMacAddress, alvarionDeviceEventNotificationGroup=alvarionDeviceEventNotificationGroup)
