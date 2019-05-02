#
# PySNMP MIB module COLUBRIS-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/COLUBRIS-TC
# Produced by pysmi-0.3.4 at Wed May  1 12:25:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
colubrisModules, = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Bits, iso, ObjectIdentity, IpAddress, NotificationType, Gauge32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter32, Counter64, Unsigned32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Bits", "iso", "ObjectIdentity", "IpAddress", "NotificationType", "Gauge32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter32", "Counter64", "Unsigned32", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
colubrisTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744, 4, 1))
if mibBuilder.loadTexts: colubrisTextualConventions.setLastUpdated('201008260000Z')
if mibBuilder.loadTexts: colubrisTextualConventions.setOrganization('Colubris Networks, Inc.')
if mibBuilder.loadTexts: colubrisTextualConventions.setContactInfo('Colubris Networks Postal: 200 West Street Ste 300 Waltham, Massachusetts 02451-1121 UNITED STATES Phone: +1 781 684 0001 Fax: +1 781 684 0009 E-mail: cn-snmp@colubris.com')
if mibBuilder.loadTexts: colubrisTextualConventions.setDescription('This module defines the Textual Conventions used in Colubris Networks enterprise MIBs.')
class ColubrisAuthenticationMode(TextualConvention, Integer32):
    description = "Specifies the authentication mode to be used. local: The authentication is done locally from the device's local database information. profile: An authentication profile is used in order to retrieve the authentication parameters. localAndProfile: The authentication is done locally first. If it fails an authentication profile is used."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("local", 1), ("profile", 2), ("localAndProfile", 3))

class ColubrisUsersAuthenticationMode(TextualConvention, Integer32):
    description = 'Specifies the authentication mode to be used. none: Users are not allowed to login. local: User authentication is done via the local user accounts. profile: A third-party authentication server is used. localAndProfile: Authentication is done locally first. If it fails, a third-party authentication server is used.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("local", 1), ("profile", 2), ("localAndProfile", 3))

class ColubrisUsersAuthenticationType(TextualConvention, Integer32):
    description = 'Specifies the authentication type to be used. mac: Users are authenticated using their MAC addresses. ieee802dot1x: Users authenticated through 802.1X. html: Users authenticated via the HTML login page.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("mac", 1), ("ieee802dot1x", 2), ("html", 3))

class ColubrisNotificationEnable(TextualConvention, Integer32):
    description = 'Specifies the generation of notification traps. enable: Enables the generation of the associated notification. disable: Disables the generation of the associated notification'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enable", 1), ("disable", 2))

class ColubrisProfileIndex(TextualConvention, Integer32):
    description = 'A profile index refers to an entry in the RADIUS server profile table.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class ColubrisProfileIndexOrZero(TextualConvention, Integer32):
    description = 'A profile index refers to an entry in the RADIUS server profile table. When the special value Zero is specified, no RADIUS server profile is selected.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class ColubrisServerIndex(TextualConvention, Integer32):
    description = 'A server index refers to an entry in the RADIUS server table.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class ColubrisServerIndexOrZero(TextualConvention, Integer32):
    description = 'A server index refers to an entry in the RADIUS server table. When the special value Zero is specified, no RADIUS server is selected.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class ColubrisSSID(TextualConvention, OctetString):
    description = 'A generic service set identifier (SSID) convention is defined here and used throughout the Colubris proprietary MIBs. This specific textual convention is used for inputing SSIDs.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

class ColubrisSSIDOrNone(TextualConvention, OctetString):
    description = 'A generic service set identifier (SSID) convention is defined here and used throughout the Colubris proprietary MIBs. This specific textual convention is used when displaying SSIDs.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class ColubrisSecurity(TextualConvention, Integer32):
    description = "An enumeration of the different Security modes allowed in the Colubris products. NOTE: 'unknown'- Could not identify the protection mode. 'none' - No wireless protection. 'wep' - WEP (static keys). 'ieee802dot1x' - 802.1X no encryption. 'ieee802dot1xWithWep' - 802.1x + WEP (dynamic keys). 'wpa' - 802.1X + TKIP + Key source AAA profile. 'wpaPsk' - 802.1X + TKIP + Key Source Pre-Shared Key."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unknown", 0), ("none", 1), ("wep", 2), ("ieee802dot1x", 3), ("ieee802dot1xWithWep", 4), ("wpa", 5), ("wpaPsk", 6))

class ColubrisPriorityQueue(TextualConvention, Integer32):
    description = 'An enumeration of the different queues supported in the QOS and Bandwidth control feature.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("low", 1), ("normal", 2), ("high", 3), ("veryHigh", 4))

class ColubrisDataRate(TextualConvention, Integer32):
    description = 'An enumeration of the different data rates supported on a per VSC basis.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
    namedValues = NamedValues(("unknown", 0), ("rateLowestAvailable", 1), ("rate1Meg", 2), ("rate2Meg", 3), ("rate5dot5Meg", 4), ("rate6Meg", 5), ("rate9Meg", 6), ("rate11Meg", 7), ("rate12Meg", 8), ("rate18Meg", 9), ("rate24Meg", 10), ("rate36Meg", 11), ("rate48Meg", 12), ("rate54Meg", 13), ("rateHighestAvailable", 14))

class ColubrisRadioType(TextualConvention, Integer32):
    description = 'An enumeration of the different supported radio types.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 5, 6, 7))
    namedValues = NamedValues(("cm6", 1), ("cm9", 2), ("sunfish", 3), ("mb82", 5), ("ar2317", 6), ("xb114", 7))

mibBuilder.exportSymbols("COLUBRIS-TC", ColubrisUsersAuthenticationMode=ColubrisUsersAuthenticationMode, ColubrisSSIDOrNone=ColubrisSSIDOrNone, ColubrisPriorityQueue=ColubrisPriorityQueue, ColubrisProfileIndexOrZero=ColubrisProfileIndexOrZero, ColubrisSSID=ColubrisSSID, ColubrisDataRate=ColubrisDataRate, colubrisTextualConventions=colubrisTextualConventions, ColubrisRadioType=ColubrisRadioType, ColubrisAuthenticationMode=ColubrisAuthenticationMode, ColubrisUsersAuthenticationType=ColubrisUsersAuthenticationType, ColubrisProfileIndex=ColubrisProfileIndex, ColubrisSecurity=ColubrisSecurity, ColubrisServerIndexOrZero=ColubrisServerIndexOrZero, ColubrisNotificationEnable=ColubrisNotificationEnable, ColubrisServerIndex=ColubrisServerIndex, PYSNMP_MODULE_ID=colubrisTextualConventions)
