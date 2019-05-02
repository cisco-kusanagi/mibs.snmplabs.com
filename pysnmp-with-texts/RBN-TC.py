#
# PySNMP MIB module RBN-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RBN-TC
# Produced by pysmi-0.3.4 at Wed May  1 14:52:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
rbnModules, = mibBuilder.importSymbols("RBN-SMI", "rbnModules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, Counter32, MibIdentifier, TimeTicks, Gauge32, ModuleIdentity, Unsigned32, iso, IpAddress, Bits, Integer32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "Counter32", "MibIdentifier", "TimeTicks", "Gauge32", "ModuleIdentity", "Unsigned32", "iso", "IpAddress", "Bits", "Integer32", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rbnTC = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352, 5, 2))
rbnTC.setRevisions(('2009-10-20 17:00', '2004-06-19 17:00', '2003-03-17 17:00', '2002-11-11 00:00', '2002-06-26 00:00', '2000-07-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rbnTC.setRevisionsDescriptions(('Added new textual convention: RbnUnsigned64 for read-write capable 64 bit integer value.', 'Added new textual convention: RbnPortMediumType. Correct warnings given by smilint.', 'Added new textual convention: RbnVidOrUntagged.', 'Moved definitions of RbnSlot and RbnPort from RBN-PVC-MIB. Updated range on RbnSlot and RbnPort.', 'Updated CONTACT-INFO. Added new textual conventions: RbnKBytes and RbnPercentage.', 'Initial version.',))
if mibBuilder.loadTexts: rbnTC.setLastUpdated('200910201700Z')
if mibBuilder.loadTexts: rbnTC.setOrganization('Redback Networks, Inc.')
if mibBuilder.loadTexts: rbnTC.setContactInfo(' RedBack Networks, Inc. Postal: 300 Holger Way San Jose, CA 95134-1362 USA Phone: +1 408 750 5000 Fax: +1 408 750 5599 E-mail: mib-info@redback.com ')
if mibBuilder.loadTexts: rbnTC.setDescription('Defines common textual conventions used in Redback mib modules.')
class RbnCircuitHandle(TextualConvention, OctetString):
    description = 'A unique identifier for individual circuits. The string is composed of the following: Octet 1 slot 2 port 3-8 circuit identifier slots/ports are numbered 0..n. The SMS CLI also numbers slots/ports 0..n but SE CLI numbers slots/ports 1..n. For example: When the SE CLI refers to slot/port 1/2, this maps to to the RbnCircuitHandle slot/port 0/1 '
    status = 'current'
    displayHint = '1d:1d:2x-2x-2x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class RbnKBytes(TextualConvention, Integer32):
    description = 'Storage size, expressed in units of 1024 bytes.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class RbnPercentage(TextualConvention, Integer32):
    description = 'This Textual Convention describes an object that stores a whole integer percentage value.'
    status = 'current'
    displayHint = 'd%'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 100)

class RbnSlot(TextualConvention, Unsigned32):
    description = "The chassis slot number. This is the physical slot number as reported in the CLI command 'show hardware' on SMS and the CLI command 'show port' on SE."
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class RbnPort(TextualConvention, Unsigned32):
    description = "The chassis port number. This is the physical port number as reported in the CLI command 'show hardware' on SMS and the CLI command 'show port' on SE."
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class RbnVidOrUntagged(TextualConvention, Integer32):
    description = 'The twelve-bit VLAN Identifer (VID) used to uniquely identify the VLAN to which the frame belongs. The VID is encoded as an unsigned binary number. An untagged frame does not carry any identification of the VLAN to which it belongs and is designated with a value of 4096.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 4096)

class RbnPortMediumType(TextualConvention, Integer32):
    description = 'Medium type of NAS port.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 11, 12, 13, 14))
    namedValues = NamedValues(("unknown", 0), ("dsl", 11), ("cable", 12), ("wireless", 13), ("satellite", 14))

class RbnUnsigned64(TextualConvention, OctetString):
    description = 'Unsigned 64 bit integer value is represented as an OCTET STRING. This allows an unsigned integer value in the range 0..18446744073709551615. The octets are ordered with the first octet containing the highest ordered bits of the integer and the 8th octet containing the lowest ordered bits, corresponding to network byte order.'
    status = 'current'
    displayHint = '8d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

mibBuilder.exportSymbols("RBN-TC", RbnSlot=RbnSlot, RbnVidOrUntagged=RbnVidOrUntagged, RbnPercentage=RbnPercentage, RbnCircuitHandle=RbnCircuitHandle, PYSNMP_MODULE_ID=rbnTC, rbnTC=rbnTC, RbnPortMediumType=RbnPortMediumType, RbnKBytes=RbnKBytes, RbnUnsigned64=RbnUnsigned64, RbnPort=RbnPort)
