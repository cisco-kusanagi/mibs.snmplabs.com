#
# PySNMP MIB module DIFFSERV-DSCP-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DIFFSERV-DSCP-TC
# Produced by pysmi-0.3.4 at Wed May  1 11:18:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, IpAddress, mib_2, NotificationType, Unsigned32, Bits, TimeTicks, Gauge32, Counter32, Counter64, iso, ModuleIdentity, Integer32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "IpAddress", "mib-2", "NotificationType", "Unsigned32", "Bits", "TimeTicks", "Gauge32", "Counter32", "Counter64", "iso", "ModuleIdentity", "Integer32", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
diffServDSCPTC = ModuleIdentity((1, 3, 6, 1, 2, 1, 96))
diffServDSCPTC.setRevisions(('2002-05-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: diffServDSCPTC.setRevisionsDescriptions(('Initial version, published as RFC 3289.',))
if mibBuilder.loadTexts: diffServDSCPTC.setLastUpdated('200205090000Z')
if mibBuilder.loadTexts: diffServDSCPTC.setOrganization('IETF Differentiated Services WG')
if mibBuilder.loadTexts: diffServDSCPTC.setContactInfo(' Fred Baker Cisco Systems 1121 Via Del Rey Santa Barbara, CA 93117, USA E-mail: fred@cisco.com Kwok Ho Chan Nortel Networks 600 Technology Park Drive Billerica, MA 01821, USA E-mail: khchan@nortelnetworks.com Andrew Smith Harbour Networks Jiuling Building 21 North Xisanhuan Ave. Beijing, 100089, PRC E-mail: ah_smith@acm.org Differentiated Services Working Group: diffserv@ietf.org')
if mibBuilder.loadTexts: diffServDSCPTC.setDescription('The Textual Conventions defined in this module should be used whenever a Differentiated Services Code Point is used in a MIB.')
class Dscp(TextualConvention, Integer32):
    reference = 'RFC 2474, RFC 2780'
    description = 'A Differentiated Services Code-Point that may be used for marking a traffic stream.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 63)

class DscpOrAny(TextualConvention, Integer32):
    reference = 'RFC 2474, RFC 2780'
    description = 'The IP header Differentiated Services Code-Point that may be used for discriminating among traffic streams. The value -1 is used to indicate a wild card i.e. any value.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 63), )
class IndexInteger(TextualConvention, Unsigned32):
    description = 'An integer which may be used as a table index.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class IndexIntegerNextFree(TextualConvention, Unsigned32):
    description = 'An integer which may be used as a new Index in a table. The special value of 0 indicates that no more new entries can be created in the relevant table. When a MIB is used for configuration, an object with this SYNTAX always contains a legal value (if non-zero) for an index that is not currently used in the relevant table. The Command Generator (Network Management Application) reads this variable and uses the (non-zero) value read when creating a new row with an SNMP SET. When the SET is performed, the Command Responder (agent) must determine whether the value is indeed still unused; Two Network Management Applications may attempt to create a row (configuration entry) simultaneously and use the same value. If it is currently unused, the SET succeeds and the Command Responder (agent) changes the value of this object, according to an implementation-specific algorithm. If the value is in use, however, the SET fails. The Network Management Application must then re-read this variable to obtain a new usable value. An OBJECT-TYPE definition using this SYNTAX MUST specify the relevant table for which the object is providing this functionality.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class IfDirection(TextualConvention, Integer32):
    description = "IfDirection specifies a direction of data travel on an interface. 'inbound' traffic is operated on during reception from the interface, while 'outbound' traffic is operated on prior to transmission on the interface."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("inbound", 1), ("outbound", 2))

mibBuilder.exportSymbols("DIFFSERV-DSCP-TC", diffServDSCPTC=diffServDSCPTC, Dscp=Dscp, IndexIntegerNextFree=IndexIntegerNextFree, DscpOrAny=DscpOrAny, IfDirection=IfDirection, PYSNMP_MODULE_ID=diffServDSCPTC, IndexInteger=IndexInteger)
