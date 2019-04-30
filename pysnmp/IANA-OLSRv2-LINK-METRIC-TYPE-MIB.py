#
# PySNMP MIB module IANA-OLSRv2-LINK-METRIC-TYPE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IANA-OLSRv2-LINK-METRIC-TYPE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:38:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, TimeTicks, ModuleIdentity, Unsigned32, Counter64, NotificationType, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Bits, mib_2, MibIdentifier, ObjectIdentity, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "TimeTicks", "ModuleIdentity", "Unsigned32", "Counter64", "NotificationType", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Bits", "mib-2", "MibIdentifier", "ObjectIdentity", "Integer32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ianaolsrv2LinkMetricType = ModuleIdentity((1, 3, 6, 1, 2, 1, 221))
ianaolsrv2LinkMetricType.setRevisions(('2014-04-09 00:00',))
if mibBuilder.loadTexts: ianaolsrv2LinkMetricType.setLastUpdated('201404090000Z')
if mibBuilder.loadTexts: ianaolsrv2LinkMetricType.setOrganization('IANA')
class IANAolsrv2LinkMetricTypeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0))
    namedValues = NamedValues(("unknown", 0))

mibBuilder.exportSymbols("IANA-OLSRv2-LINK-METRIC-TYPE-MIB", IANAolsrv2LinkMetricTypeTC=IANAolsrv2LinkMetricTypeTC, PYSNMP_MODULE_ID=ianaolsrv2LinkMetricType, ianaolsrv2LinkMetricType=ianaolsrv2LinkMetricType)
