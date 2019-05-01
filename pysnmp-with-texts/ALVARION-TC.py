#
# PySNMP MIB module ALVARION-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALVARION-TC
# Produced by pysmi-0.3.4 at Wed May  1 11:21:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
alvarionModules, = mibBuilder.importSymbols("ALVARION-SMI", "alvarionModules")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, ModuleIdentity, TimeTicks, iso, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Bits, Counter32, MibIdentifier, IpAddress, Integer32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ModuleIdentity", "TimeTicks", "iso", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Bits", "Counter32", "MibIdentifier", "IpAddress", "Integer32", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
alvarionTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 12394, 1, 10, 4, 1))
if mibBuilder.loadTexts: alvarionTextualConventions.setLastUpdated('200710310000Z')
if mibBuilder.loadTexts: alvarionTextualConventions.setOrganization('Alvarion Ltd.')
if mibBuilder.loadTexts: alvarionTextualConventions.setContactInfo('Alvarion Ltd. Postal: 21a HaBarzel St. P.O. Box 13139 Tel-Aviv 69710 Israel Phone: +972 3 645 6262')
if mibBuilder.loadTexts: alvarionTextualConventions.setDescription('This module defines the Textual Conventions used in Alvarion enterprise MIBs.')
class AlvarionAuthenticationMode(TextualConvention, Integer32):
    description = 'Specifies the authentication mode to be used. local: The authentication is done locally from the device local database information. profile: An AAA profile is used in order to retrieve the authentication parameters.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("local", 1), ("profile", 2))

class AlvarionUsersAuthenticationMode(TextualConvention, Integer32):
    description = 'Specifies the authentication mode to be used. none: Users are not allowed to login. local: The authentication is done locally from the device local database information. profile: An AAA profile is used in order to retrieve the authentication parameters. localAndProfile: The authentication is done locally first. If it fails an AAA profile is used.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("local", 1), ("profile", 2), ("localAndProfile", 3))

class AlvarionUsersAuthenticationType(TextualConvention, Integer32):
    description = 'Specifies the authentication type to be used. mac: Users authenticated using their MAC addresses. ieee802dot1x: Users authenticated through 802.1x. html: Users authenticated with html.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("mac", 1), ("ieee802dot1x", 2), ("html", 3))

class AlvarionNotificationEnable(TextualConvention, Integer32):
    description = 'Specifies the generation of notification traps. enable: Enable the generation of the associated notification. disable: Disables the generation of the associated notification'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enable", 1), ("disable", 2))

class AlvarionProfileIndex(TextualConvention, Integer32):
    description = 'A profile index refers to an entry in the AAA profile table.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class AlvarionProfileIndexOrZero(TextualConvention, Integer32):
    description = 'A profile index refers to an entry in the AAA profile table. When the special value Zero is specified, no AAA server profile is selected.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class AlvarionServerIndex(TextualConvention, Integer32):
    description = 'A server index refers to an entry in the AAA server table.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class AlvarionServerIndexOrZero(TextualConvention, Integer32):
    description = 'A server index refers to an entry in the AAA server table. When the special value Zero is specified, no AAA server is selected.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class AlvarionSSID(TextualConvention, OctetString):
    description = 'A generic service set identifier (SSID) convention is defined here and used throughout the Alvarion proprietary MIBs. This specific textual convention is used for inputing SSIDs.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

class AlvarionSSIDOrNone(TextualConvention, OctetString):
    description = 'A generic service set identifier (SSID) convention is defined here and used throughout the Alvarion proprietary MIBs. This specific textual convention is used when displaying SSIDs.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class AlvarionSecurity(TextualConvention, Integer32):
    description = "An enumeration of the different Security modes allowed in the Alvarion products. NOTE: 'unknown'- Could not identify the protection mode. 'none' - No wireless protection. 'wep' - WEP (static keys). 'ieee802dot1x' - 802.1x no encryption. 'ieee802dot1xWithWep' - 802.1x + WEP (dynamic keys). 'wpa' - 802.1x + TKIP + Key source AAA profile. 'wpaPsk' - 802.1x + TKIP + Key Source Pre-Shared Key."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unknown", 0), ("none", 1), ("wep", 2), ("ieee802dot1x", 3), ("ieee802dot1xWithWep", 4), ("wpa", 5), ("wpaPsk", 6))

class AlvarionPriorityQueue(TextualConvention, Integer32):
    description = 'An enumeration of the different queues supported in the QOS and Bandwidth control feature of the Alvarion products.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("low", 1), ("normal", 2), ("high", 3), ("veryHigh", 4))

class AlvarionDataRate(TextualConvention, Integer32):
    description = 'An enumeration of the different data rates supported on a per VAP basis.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
    namedValues = NamedValues(("rateLowestAvailable", 1), ("rate1Meg", 2), ("rate2Meg", 3), ("rate5dot5Meg", 4), ("rate6Meg", 5), ("rate9Meg", 6), ("rate11Meg", 7), ("rate12Meg", 8), ("rate18Meg", 9), ("rate24Meg", 10), ("rate36Meg", 11), ("rate48Meg", 12), ("rate54Meg", 13), ("rateHighestAvailable", 14))

class AlvarionRadioType(TextualConvention, Integer32):
    description = 'An enumeration of the different radio types used in the Alvarion products.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("cm6", 1), ("cm9", 2), ("sunfish", 3), ("wi2", 4))

mibBuilder.exportSymbols("ALVARION-TC", AlvarionPriorityQueue=AlvarionPriorityQueue, AlvarionRadioType=AlvarionRadioType, PYSNMP_MODULE_ID=alvarionTextualConventions, AlvarionSecurity=AlvarionSecurity, AlvarionServerIndex=AlvarionServerIndex, AlvarionSSID=AlvarionSSID, AlvarionDataRate=AlvarionDataRate, AlvarionAuthenticationMode=AlvarionAuthenticationMode, AlvarionProfileIndexOrZero=AlvarionProfileIndexOrZero, AlvarionUsersAuthenticationType=AlvarionUsersAuthenticationType, AlvarionProfileIndex=AlvarionProfileIndex, AlvarionSSIDOrNone=AlvarionSSIDOrNone, AlvarionUsersAuthenticationMode=AlvarionUsersAuthenticationMode, AlvarionNotificationEnable=AlvarionNotificationEnable, alvarionTextualConventions=alvarionTextualConventions, AlvarionServerIndexOrZero=AlvarionServerIndexOrZero)
