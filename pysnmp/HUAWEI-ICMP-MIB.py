#
# PySNMP MIB module HUAWEI-ICMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-ICMP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:33:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
huawei, hwInternetProtocol, hwLocal = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "huawei", "hwInternetProtocol", "hwLocal")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, TimeTicks, MibIdentifier, enterprises, Counter64, ModuleIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter32, IpAddress, Integer32, Gauge32, NotificationType, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "TimeTicks", "MibIdentifier", "enterprises", "Counter64", "ModuleIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter32", "IpAddress", "Integer32", "Gauge32", "NotificationType", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rIcmp = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 1, 3, 2))
icmpInBadCode = MibScalar((1, 3, 6, 1, 4, 1, 2011, 1, 3, 2, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icmpInBadCode.setStatus('mandatory')
icmpInBadLen = MibScalar((1, 3, 6, 1, 4, 1, 2011, 1, 3, 2, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icmpInBadLen.setStatus('mandatory')
icmpInChecksum = MibScalar((1, 3, 6, 1, 4, 1, 2011, 1, 3, 2, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icmpInChecksum.setStatus('mandatory')
icmpInTooShort = MibScalar((1, 3, 6, 1, 4, 1, 2011, 1, 3, 2, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icmpInTooShort.setStatus('mandatory')
icmpOutOldIcmp = MibScalar((1, 3, 6, 1, 4, 1, 2011, 1, 3, 2, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icmpOutOldIcmp.setStatus('mandatory')
icmpOutShort = MibScalar((1, 3, 6, 1, 4, 1, 2011, 1, 3, 2, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icmpOutShort.setStatus('mandatory')
mibBuilder.exportSymbols("HUAWEI-ICMP-MIB", icmpInChecksum=icmpInChecksum, icmpInTooShort=icmpInTooShort, icmpOutShort=icmpOutShort, icmpInBadLen=icmpInBadLen, icmpInBadCode=icmpInBadCode, icmpOutOldIcmp=icmpOutOldIcmp, rIcmp=rIcmp)
