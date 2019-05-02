#
# PySNMP MIB module IANA-OLSRv2-LINK-METRIC-TYPE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IANA-OLSRv2-LINK-METRIC-TYPE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:50:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter32, NotificationType, iso, Counter64, IpAddress, Gauge32, mib_2, Bits, Integer32, ObjectIdentity, TimeTicks, MibIdentifier, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter32", "NotificationType", "iso", "Counter64", "IpAddress", "Gauge32", "mib-2", "Bits", "Integer32", "ObjectIdentity", "TimeTicks", "MibIdentifier", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ianaolsrv2LinkMetricType = ModuleIdentity((1, 3, 6, 1, 2, 1, 221))
ianaolsrv2LinkMetricType.setRevisions(('2014-04-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ianaolsrv2LinkMetricType.setRevisionsDescriptions(('Initial version of this MIB as published in RFC 7184.',))
if mibBuilder.loadTexts: ianaolsrv2LinkMetricType.setLastUpdated('201404090000Z')
if mibBuilder.loadTexts: ianaolsrv2LinkMetricType.setOrganization('IANA')
if mibBuilder.loadTexts: ianaolsrv2LinkMetricType.setContactInfo('Internet Assigned Numbers Authority Postal: ICANN 12025 Waterfront Drive, Suite 300 Los Angeles, CA 90094-2536 Tel: +1 310 301 5800 E-Mail: iana&iana.org')
if mibBuilder.loadTexts: ianaolsrv2LinkMetricType.setDescription('This MIB module defines the IANAolsrv2LinkMetricType Textual Convention, and thus the enumerated values of the olsrv2LinkMetricType object defined in the OLSRv2-MIB.')
class IANAolsrv2LinkMetricTypeTC(TextualConvention, Integer32):
    description = "This data type is used as the syntax of the olsrv2LinkMetricType object in the definition of the OLSRv2-MIB module. The olsrv2LinkMetricType corresponds to LINK_METRIC_TYPE of OLSRv2 (RFC 7181). OLSRv2 uses bidirectional additive link metrics to determine shortest distance routes (i.e., routes with smallest total of link metric values). OLSRv2 has established a registry for the LINK_METRIC_TYPEs (denoted 'LINK_METRIC Address Block TLV Type Extensions'): http://www.iana.org/assignments/manet-parameters/ This is done in Section 24.5 in OLSRv2 (RFC 7181). The LINK_METRIC_TYPE (which has as corresponding object in the MIB module olsrv2LinkMetricType) corresponds to the type extension of the LINK_METRIC TLV that is set up in the 'LINK_METRIC Address Block TLV Type Extensions' registry. Whenever new link metric types are added to that registry, IANA MUST update this textual convention accordingly. The definition of this textual convention with the addition of newly assigned values is published periodically by the IANA, in either the Assigned Numbers RFC, or some derivative of it specific to Internet Network Management number assignments. (The latest arrangements can be obtained by contacting the IANA.) Requests for new values should be made to IANA via email (iana&iana.org)."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0))
    namedValues = NamedValues(("unknown", 0))

mibBuilder.exportSymbols("IANA-OLSRv2-LINK-METRIC-TYPE-MIB", ianaolsrv2LinkMetricType=ianaolsrv2LinkMetricType, PYSNMP_MODULE_ID=ianaolsrv2LinkMetricType, IANAolsrv2LinkMetricTypeTC=IANAolsrv2LinkMetricTypeTC)
