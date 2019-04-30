#
# PySNMP MIB module IANA-MALLOC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IANA-MALLOC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:38:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Counter64, Unsigned32, MibIdentifier, iso, Bits, NotificationType, Gauge32, Integer32, ObjectIdentity, mib_2, ModuleIdentity, IpAddress, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Counter64", "Unsigned32", "MibIdentifier", "iso", "Bits", "NotificationType", "Gauge32", "Integer32", "ObjectIdentity", "mib-2", "ModuleIdentity", "IpAddress", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ianaMallocMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 102))
ianaMallocMIB.setRevisions(('2014-05-22 00:00', '2003-01-27 12:00',))
if mibBuilder.loadTexts: ianaMallocMIB.setLastUpdated('201405220000Z')
if mibBuilder.loadTexts: ianaMallocMIB.setOrganization('IANA')
class IANAscopeSource(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("other", 1), ("manual", 2), ("local", 3), ("mzap", 4), ("madcap", 5))

class IANAmallocRangeSource(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("other", 1), ("manual", 2), ("local", 3))

mibBuilder.exportSymbols("IANA-MALLOC-MIB", PYSNMP_MODULE_ID=ianaMallocMIB, ianaMallocMIB=ianaMallocMIB, IANAscopeSource=IANAscopeSource, IANAmallocRangeSource=IANAmallocRangeSource)
