#
# PySNMP MIB module RTBRICK-PRODUCTS (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/tin/Dev/mibs.snmplabs.com/asn1/RTBRICK-PRODUCTS-MIB
# Produced by pysmi-0.3.4 at Fri Jan 31 21:35:45 2020
# On host bier platform Linux version 5.4.0-3-amd64 by user tin
# Using Python version 3.7.6 (default, Jan 19 2020, 22:34:52) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
rtbrickProducts, rtbrickModules = mibBuilder.importSymbols("RTBRICK-MIB", "rtbrickProducts", "rtbrickModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Counter64, IpAddress, enterprises, Integer32, NotificationType, ModuleIdentity, Bits, ObjectIdentity, MibIdentifier, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter64", "IpAddress", "enterprises", "Integer32", "NotificationType", "ModuleIdentity", "Bits", "ObjectIdentity", "MibIdentifier", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter32", "iso")
AutonomousType, TimeStamp, TestAndIncr, TextualConvention, TruthValue, RowStatus, DisplayString, PhysAddress = mibBuilder.importSymbols("SNMPv2-TC", "AutonomousType", "TimeStamp", "TestAndIncr", "TextualConvention", "TruthValue", "RowStatus", "DisplayString", "PhysAddress")
rtbrickProductsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 50058, 104, 1))
rtbrickProductsMIB.setRevisions(('2018-04-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rtbrickProductsMIB.setRevisionsDescriptions(('Initial revision',))
if mibBuilder.loadTexts: rtbrickProductsMIB.setLastUpdated('201804140000Z')
if mibBuilder.loadTexts: rtbrickProductsMIB.setOrganization('RtBrick')
if mibBuilder.loadTexts: rtbrickProductsMIB.setContactInfo('E-mail: Stefan Lieberth <stefan@rtbrick.com>')
if mibBuilder.loadTexts: rtbrickProductsMIB.setDescription('RtBrick Product Information')
rtbrickECAS591654XK = MibIdentifier((1, 3, 6, 1, 4, 1, 50058, 102, 1))
mibBuilder.exportSymbols("RTBRICK-PRODUCTS", rtbrickProductsMIB=rtbrickProductsMIB, PYSNMP_MODULE_ID=rtbrickProductsMIB, rtbrickECAS591654XK=rtbrickECAS591654XK)
