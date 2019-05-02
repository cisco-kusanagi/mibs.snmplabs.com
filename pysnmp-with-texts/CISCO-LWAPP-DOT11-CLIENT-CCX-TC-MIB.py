#
# PySNMP MIB module CISCO-LWAPP-DOT11-CLIENT-CCX-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-LWAPP-DOT11-CLIENT-CCX-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:05:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, MibIdentifier, NotificationType, ObjectIdentity, Unsigned32, TimeTicks, Integer32, Bits, Counter32, Gauge32, Counter64, IpAddress, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibIdentifier", "NotificationType", "ObjectIdentity", "Unsigned32", "TimeTicks", "Integer32", "Bits", "Counter32", "Gauge32", "Counter64", "IpAddress", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoLwappDot11ClientCCXTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 611))
ciscoLwappDot11ClientCCXTextualConventions.setRevisions(('2007-03-22 00:00', '2007-02-22 00:00', '2007-02-19 00:00', '2007-01-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoLwappDot11ClientCCXTextualConventions.setRevisionsDescriptions(('Added 2 more radio types to CiscoLwappDot11ClientRadioType.', 'Reverted some of the enum names to be in line with the CCXV5 spec.', 'Incorporated review comments.', 'Initial version of this mib module.',))
if mibBuilder.loadTexts: ciscoLwappDot11ClientCCXTextualConventions.setLastUpdated('200703220000Z')
if mibBuilder.loadTexts: ciscoLwappDot11ClientCCXTextualConventions.setOrganization('Cisco Systems Inc.')
if mibBuilder.loadTexts: ciscoLwappDot11ClientCCXTextualConventions.setContactInfo('Cisco Systems, Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS Email: cs-wnbu-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoLwappDot11ClientCCXTextualConventions.setDescription("This module defines the textual conventions used throughout the Cisco enterprise MIBs designed for implementation on Central Controllers (CC) that terminate the Light Weight Access Point Protocol tunnel from Light-weight LWAPP Access Points, specifically for the functions of the Cisco Client Extensions (CCX) program. This MIB provides textual conventions used in the configuration and status information mibs about the CCX clients that the controller is aware of. GLOSSARY Light Weight Access Point Protocol ( LWAPP ) This is a generic protocol that defines the communication between the Access Points and the Central Controller. Mobile Node ( MN ) A roaming 802.11 wireless device in a wireless network associated with an access point. Mobile Node, Mobile Station(Ms) and client are used interchangeably. Cisco Client eXtentions (CCX) The Cisco Client Extensions (CCX) Program is a program of working through silicon providers to embed Cisco client technology in wireless client reference designs, and to promote compliant and interoperable third-party clients with Cisco's infrastructure, thus further driving wireless adoption in the market. Extensible Authentication Protocol (EAP) The Extensible Authentication Protocol (EAP) is an Internet Engineering Task Force (IETF) standard that provides an infrastructure for network access clients and authentication servers to host plug-in modules for current and future authentication methods and technologies. Wired Equivalent Privacy (WEP) A security method defined by 802.11. WEP uses a symmetric key stream cipher called RC4 to encrypt the data packets. REFERENCE [1] Part 11 Wireless LAN Medium Access Control ( MAC ) and Physical Layer ( PHY ) Specifications. [2] Draft-obara-capwap-lwapp-00.txt, IETF Light Weight Access Point Protocol. [3] Cisco Compatible Extensions for WLAN Devices Version 5.0.11")
class CiscoLwappDot11ClientReqStatus(TextualConvention, Integer32):
    description = 'This field indicates the status of current request.The values used can be one of the following: initiate - this will be used to trigger a request to get some parameters from a CCX client. inProgress - this indicates that the request to get the details from the client is still in progress. success - indicates that the query was executed successfully. failed - this indicates that the request to get some parameters from a CCX client failed. requestNotProcessedByClient - indicates that the CCX client did not honour this request.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("initiate", 1), ("inProgress", 2), ("success", 3), ("failure", 4), ("requestNotProcessedByClient", 5))

class CiscoLwappDot11ClientSSId(TextualConvention, OctetString):
    description = 'This represents the Service Set Identifier assigned to WLAN.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

class CiscoLwappDot11ClientAuthMethod(TextualConvention, Integer32):
    description = 'This is the authentication method used by the client. The possible values are: none - this indicates that no authentication method is used preSharedKey - this refers to the method of using pre shared key for authentication eap - this is Extensible Authentication Protocol unknown - this indicates an authentication protocol other than the ones defined above'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 255))
    namedValues = NamedValues(("none", 0), ("preSharedKey", 1), ("eap", 2), ("unknown", 255))

class CiscoLwappDot11ClientEAPMethod(TextualConvention, Integer32):
    description = 'This identifies the Extensible Authentication Protocol(EAP) method used. The possible values are: leap - this is Lightweight Extensible Authentication Protocol eapFast - this is Extensible Authentication Protocol with Flexible Authentication via Secure Tunneling eapTls - this is Extensible Authentication Protocol with Transport Layer Security eapTtls - this is Extensible Authentication Protocol with Tunneled Transport Layer Security peap0EapMschap2 - this refers to Protected Extensible Authentication Protocol Version 0 with Microsoft Challenge Handshake Authentication Protocol version 2 peap1EapGtc - this refers to Protected Extensible Authentication Protocol Version 1 with Generic Token Card eapMd5 - this is Extensible Authentication Protocol with Message-Digest algorithm 5 eapSim - this is Extensible Authentication Protocol using the Global System for Mobile Communications (GSM) Subscriber Identity Module (SIM) preSharedKey - this refers to the method of using pre shared key for authentication unknown - this indicates an EAP method other than the ones defined above'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 255))
    namedValues = NamedValues(("leap", 0), ("eapFast", 1), ("eapTls", 2), ("eapTtls", 3), ("peap0EapMschap2", 4), ("peap1EapGtc", 5), ("eapMd5", 6), ("eapSim", 7), ("preSharedKey", 8), ("unknown", 255))

class CiscoLwappDot11ClientKeyMgmtMethod(TextualConvention, Integer32):
    description = 'This is the key management method used by the client. The possible values are: staticWep - this is Wired Equivalent Privacy with a static key defined dynamicWep - this is Wired Equivalent Privacy with a dynamic key wpa - this indicates wifi protected access wpaCckm - this is wifi protected access with Cisco Centralized Key Management wpa2 - this indicates version 2 of wifi protected access wpa2Cckm - this is wifi protected access version 2 with Cisco Centralized Key Management cckm - this indicates Cisco Centralized Key Management unknown - this indicates a key management method other than the ones defined above'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 255))
    namedValues = NamedValues(("none", 0), ("staticWep", 1), ("dynamicWep", 2), ("wpa", 3), ("wpaCckm", 4), ("wpa2", 5), ("wpa2Cckm", 6), ("cckm", 7), ("unknown", 255))

class CiscoLwappDot11ClientEncryptionMethod(TextualConvention, Integer32):
    description = 'This is the encryption method used by the client. The possible values are: none - no encryption is used wep40 - this is Wired Equivalent Privacy with a 40 bit secret key wep104 - this is Wired Equivalent Privacy with a 104 bit secret key tkip - this indicates Temporal Key Integrity Protocol ckip - this is Cisco Key Integrity Protocol aesCcmp - this is Advanced Encryption Standard - Counter Mode Cipher Block Chaining-Message Authentication Code Protocol unknown - this indicates an encryption method other than the ones defined above'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 255))
    namedValues = NamedValues(("none", 0), ("wep40", 1), ("wep104", 2), ("tkip", 3), ("ckip", 4), ("aesCcmp", 5), ("unknown", 255))

class CiscoLwappDot11ClientCredentialType(TextualConvention, Integer32):
    description = "This indicates how the 802.11 credentials are configured for the client. The possible values are: localSaved - credentials are locally saved manuallyPrompted - client is prompted for the credentials hostOsLogin - this means the host operating system's login credentials will be used unknown - this indicates a credential method other than the ones defined above"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 255))
    namedValues = NamedValues(("localSaved", 0), ("manuallyPrompted", 1), ("hostOsLogin", 2), ("unknown", 255))

class CiscoLwappDot11ClientPowerSaveMode(TextualConvention, Integer32):
    description = 'This is the type of power save mode configured on the client. The possible values are: awake - this indicates that the client is constantly awake normal - this indicates normal power save mode maxPower - this indicates maximum power save mode uApsd - this indicates Unsolicited Automatic Power Save Delivery sApsd - this indicates Solicited Automatic Power Save Delivery unknown - this indicates a power save mode other than the ones defined above'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 255))
    namedValues = NamedValues(("awake", 0), ("normal", 1), ("maxPower", 2), ("uApsd", 3), ("sApsd", 4), ("unknown", 255))

class CiscoLwappDot11ClientTxPowerMode(TextualConvention, Integer32):
    description = 'This field identifies the transmit power mode of the client. The possible values are: fixed - this indicates that the client is operating at a fixed power mode automatic - this indicates that the client power will be determined automatically'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("fixed", 0), ("automatic", 1))

class CiscoLwappDot11ClientRadioType(TextualConvention, Integer32):
    description = 'This is the radio type of the client. The possible values are: unused - this is currently a reserved radio type and is not used fhss - this is Frequency-hopping spread spectrum based radio dsss - this is Direct Sequence spread spectrum based radio infraRedBaseband - this is infrared baseband based radio oFdm - this is orthogonal frequency division multiplexing based radio highRateDsss - this is high rate direct sequence spread spectrum based radio erp - this indicates effective radiated power based radio draft11n2point4Ghz - this indicates a 2.4 Ghz band radio as defined in draft 802.11n draft11n5Ghz - this indicates a 5 Ghz band radio as defined in draft 802.11n'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("unused", 0), ("fhss", 1), ("dsss", 2), ("irBaseband", 3), ("oFdm", 4), ("highRateDsss", 5), ("erp", 6), ("draft11n2point4Ghz", 7), ("draft11n5Ghz", 8))

class CiscoLwappDot11ClientDataRates(TextualConvention, Bits):
    description = 'This field indicates the data rates supported by a client. If a data rate is supported by a client, the corresponding bit is set to 1 else it is set to 0. The different data rates (in Mhz) are 1, 2, 5.5, 6, 9, 11, 12, 18, 24, 36, 48, 54.'
    status = 'current'
    namedValues = NamedValues(("mhz1", 0), ("mhz2", 1), ("mhz5point5", 2), ("mhz6", 3), ("mhz9", 4), ("mhz11", 5), ("mhz12", 6), ("mhz18", 7), ("mhz24", 8), ("mhz36", 9), ("mhz48", 10), ("mhz54", 11))

class CLDot11ClientDiagAssocReason(TextualConvention, Integer32):
    description = 'This field indicates the reason for which the client has to be associated to a diagnostic WLAN.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("reconnect", 0), ("unreliableLink", 1), ("dot11AuthFail", 2), ("dot11AssocFail", 3), ("rsnaFail", 4), ("dhcpFail", 5), ("dnsFail", 6), ("ipConnectivityFail", 7), ("dot1xAuthFail", 8), ("commonEapNegotiationFail", 9), ("userInitiatedReasonUnknown", 10), ("executingTest", 11), ("reserved", 12))

mibBuilder.exportSymbols("CISCO-LWAPP-DOT11-CLIENT-CCX-TC-MIB", ciscoLwappDot11ClientCCXTextualConventions=ciscoLwappDot11ClientCCXTextualConventions, CiscoLwappDot11ClientReqStatus=CiscoLwappDot11ClientReqStatus, PYSNMP_MODULE_ID=ciscoLwappDot11ClientCCXTextualConventions, CiscoLwappDot11ClientSSId=CiscoLwappDot11ClientSSId, CiscoLwappDot11ClientEAPMethod=CiscoLwappDot11ClientEAPMethod, CLDot11ClientDiagAssocReason=CLDot11ClientDiagAssocReason, CiscoLwappDot11ClientKeyMgmtMethod=CiscoLwappDot11ClientKeyMgmtMethod, CiscoLwappDot11ClientEncryptionMethod=CiscoLwappDot11ClientEncryptionMethod, CiscoLwappDot11ClientRadioType=CiscoLwappDot11ClientRadioType, CiscoLwappDot11ClientPowerSaveMode=CiscoLwappDot11ClientPowerSaveMode, CiscoLwappDot11ClientDataRates=CiscoLwappDot11ClientDataRates, CiscoLwappDot11ClientCredentialType=CiscoLwappDot11ClientCredentialType, CiscoLwappDot11ClientTxPowerMode=CiscoLwappDot11ClientTxPowerMode, CiscoLwappDot11ClientAuthMethod=CiscoLwappDot11ClientAuthMethod)
