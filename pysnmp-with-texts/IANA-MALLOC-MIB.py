#
# PySNMP MIB module IANA-MALLOC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IANA-MALLOC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:50:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, NotificationType, TimeTicks, mib_2, ObjectIdentity, Bits, Counter64, Gauge32, Unsigned32, ModuleIdentity, Counter32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "NotificationType", "TimeTicks", "mib-2", "ObjectIdentity", "Bits", "Counter64", "Gauge32", "Unsigned32", "ModuleIdentity", "Counter32", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ianaMallocMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 102))
ianaMallocMIB.setRevisions(('2014-05-22 00:00', '2003-01-27 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ianaMallocMIB.setRevisionsDescriptions(('Updated contact info.', 'Initial version.',))
if mibBuilder.loadTexts: ianaMallocMIB.setLastUpdated('201405220000Z')
if mibBuilder.loadTexts: ianaMallocMIB.setOrganization('IANA')
if mibBuilder.loadTexts: ianaMallocMIB.setContactInfo(' Internet Assigned Numbers Authority Internet Corporation for Assigned Names and Numbers 12025 Waterfront Drive, Suite 300 Los Angeles, CA 90094-2536 Phone: +1 310-301-5800 EMail: iana&iana.org')
if mibBuilder.loadTexts: ianaMallocMIB.setDescription('This MIB module defines the IANAscopeSource and IANAmallocRangeSource textual conventions for use in MIBs which need to identify ways of learning multicast scope and range information. Any additions or changes to the contents of this MIB module require either publication of an RFC, or Designated Expert Review as defined in the Guidelines for Writing IANA Considerations Section document. The Designated Expert will be selected by the IESG Area Director(s) of the Transport Area.')
class IANAscopeSource(TextualConvention, Integer32):
    description = 'The source of multicast scope information.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("other", 1), ("manual", 2), ("local", 3), ("mzap", 4), ("madcap", 5))

class IANAmallocRangeSource(TextualConvention, Integer32):
    description = 'The source of multicast address allocation range information.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("other", 1), ("manual", 2), ("local", 3))

mibBuilder.exportSymbols("IANA-MALLOC-MIB", IANAmallocRangeSource=IANAmallocRangeSource, IANAscopeSource=IANAscopeSource, ianaMallocMIB=ianaMallocMIB, PYSNMP_MODULE_ID=ianaMallocMIB)
