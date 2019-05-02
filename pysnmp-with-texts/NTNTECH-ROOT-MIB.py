#
# PySNMP MIB module NTNTECH-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NTNTECH-ROOT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:25:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Counter64, ObjectIdentity, ModuleIdentity, IpAddress, Bits, TimeTicks, Integer32, MibIdentifier, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, NotificationType, Unsigned32, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "ObjectIdentity", "ModuleIdentity", "IpAddress", "Bits", "TimeTicks", "Integer32", "MibIdentifier", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "NotificationType", "Unsigned32", "enterprises")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ntntechRootMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8059))
ntntechRootMIB.setRevisions(('1902-08-28 11:57', '1902-10-22 02:00', '1904-10-11 01:01', '1904-11-17 10:09',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ntntechRootMIB.setRevisionsDescriptions(('New Release - v1.01.00', 'New Release - v1.01.01', 'Updated copyright and references to Paradyne. Added in QoS Mib branch for future mib support. Added in a new Textual-Convention NTNTruthValue', 'New Release -- version 1.02.01',))
if mibBuilder.loadTexts: ntntechRootMIB.setLastUpdated('0411170200Z')
if mibBuilder.loadTexts: ntntechRootMIB.setOrganization('Paradyne Corporation')
if mibBuilder.loadTexts: ntntechRootMIB.setContactInfo('Paradyne Corporation 8545 126th Avenue North Largo, FL 33773 phone: +1 (727) 530-2000 email: support@paradyne.com www: http://www.nettonet.com/support/')
if mibBuilder.loadTexts: ntntechRootMIB.setDescription("This module provides explicit definitions for the Paradyne Corporation's Net to Net Technologies naming tree. Product type: Digital Subscriber Line (DSL)")
class NtnIpAddress(TextualConvention, OctetString):
    description = 'Represents the value used to define the system Ip address.'
    status = 'current'
    displayHint = '1x:2x:3x:4x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class NtnDefaultGateway(TextualConvention, OctetString):
    description = 'Represents the value used to define the system default gateway.'
    status = 'current'
    displayHint = '1x:2x:3x:4x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class NtnSubnetMask(TextualConvention, OctetString):
    description = 'Represents the value used to define the subnet address.'
    status = 'current'
    displayHint = '1x:2x:3x:4x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class NtnDisplayString(TextualConvention, OctetString):
    description = "Represents textual information taken from the NVT ASCII character set, as defined in pages 4, 10-11 of RFC 854. To summarize RFC 854, the NVT ASCII repertoire specifies: - the use of character codes 0-127 (decimal) - the graphics characters (32-126) are interpreted as US ASCII - NUL, LF, CR, BEL, BS, HT, VT and FF have the special meanings specified in RFC 854 - the other 25 codes have no standard interpretation - the sequence 'CR LF' means newline - the sequence 'CR NUL' means carriage-return - an 'LF' not preceded by a 'CR' means moving to the same column on the next line. - the sequence 'CR x' for any x other than LF or NUL is illegal. (Note that this also means that a string may end with either 'CR LF' or 'CR NUL', but not with CR.) Any object defined using this syntax may not exceed 128 characters in length."
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 127)

class NtnMacAddress(TextualConvention, OctetString):
    description = "Represents an 802 MAC address represented in the 'canonical' order defined by IEEE 802.1a, i.e., as if it were transmitted least significant bit first, even though 802.5 (in contrast to other 802.x protocols) requires MAC addresses to be transmitted most significant bit first."
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class NtnTimeTicks(TextualConvention, Integer32):
    description = 'The TimeTicks type represents a non-negative integer which represents the time, modulo 2^32 (4294967296 decimal), in hundredths of a second between two epochs. When objects are defined which use this ASN.1 type, the description of the object identifies both of the reference epochs.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class NtnCounter32(TextualConvention, Integer32):
    description = 'The NtnCounter32 type represents a non-negative integer which monotonically increases until it reaches a maximum value of 2^32-1 (4294967295 decimal), when it wraps around and starts increasing again from zero. Discontinuities in the monotonically increasing value normally occur at re-initialization of the management system.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class NtnGauge32(TextualConvention, Integer32):
    description = 'The Gauge32 type represents a non-negative integer, which may increase or decrease, but shall never exceed a maximum value. The maximum value can not be greater than 2^32-1 (4294967295 decimal). The value of a Gauge has its maximum value whenever the information being modeled is greater or equal to that maximum value; if the information being modeled subsequently decreases below the maximum value, the Gauge also decreases.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class NtnTruthValue(TextualConvention, Integer32):
    description = ' Represents the boolean yes (1) or no (2) '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("yes", 1), ("no", 2))

ntntechNamingTree = MibIdentifier((1, 3, 6, 1, 4, 1, 8059, 1))
ntntechChassis = MibIdentifier((1, 3, 6, 1, 4, 1, 8059, 1, 1))
ntntechChassisConfigurationMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1))
ntntechChassisStatusMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 8059, 1, 1, 2))
ntntechInterfaceModule = MibIdentifier((1, 3, 6, 1, 4, 1, 8059, 1, 2))
ntntechInterfaceModuleConfigurationMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 8059, 1, 2, 1))
ntntechInterfaceModuleStatusMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 8059, 1, 2, 2))
ntntechQoSMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 8059, 1, 2, 3))
ntntechNMSTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 8059, 1, 3))
ntntechNMSTrapsMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 8059, 1, 3, 1))
ntntechSystemObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8059, 1, 4))
ntntechSystemObjectsIdentifierMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 8059, 1, 4, 1))
mibBuilder.exportSymbols("NTNTECH-ROOT-MIB", ntntechChassis=ntntechChassis, PYSNMP_MODULE_ID=ntntechRootMIB, ntntechQoSMIB=ntntechQoSMIB, ntntechNMSTrapsMIB=ntntechNMSTrapsMIB, ntntechChassisStatusMIB=ntntechChassisStatusMIB, NtnDefaultGateway=NtnDefaultGateway, NtnSubnetMask=NtnSubnetMask, ntntechInterfaceModuleConfigurationMIB=ntntechInterfaceModuleConfigurationMIB, ntntechInterfaceModule=ntntechInterfaceModule, ntntechSystemObjectsIdentifierMIB=ntntechSystemObjectsIdentifierMIB, NtnMacAddress=NtnMacAddress, ntntechInterfaceModuleStatusMIB=ntntechInterfaceModuleStatusMIB, NtnCounter32=NtnCounter32, NtnTimeTicks=NtnTimeTicks, ntntechRootMIB=ntntechRootMIB, NtnDisplayString=NtnDisplayString, ntntechSystemObjects=ntntechSystemObjects, NtnGauge32=NtnGauge32, ntntechChassisConfigurationMIB=ntntechChassisConfigurationMIB, ntntechNMSTraps=ntntechNMSTraps, NtnTruthValue=NtnTruthValue, NtnIpAddress=NtnIpAddress, ntntechNamingTree=ntntechNamingTree)
