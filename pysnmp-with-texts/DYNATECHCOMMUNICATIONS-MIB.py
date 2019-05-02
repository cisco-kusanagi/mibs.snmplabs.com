#
# PySNMP MIB module DYNATECHCOMMUNICATIONS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DYNATECHCOMMUNICATIONS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:51:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, enterprises, NotificationType, Unsigned32, Integer32, IpAddress, MibIdentifier, Counter64, Bits, iso, Gauge32, ObjectIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "enterprises", "NotificationType", "Unsigned32", "Integer32", "IpAddress", "MibIdentifier", "Counter64", "Bits", "iso", "Gauge32", "ObjectIdentity", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dynatechCommunications = MibIdentifier((1, 3, 6, 1, 4, 1, 384))
dynaCommProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 384, 1))
cpx = MibIdentifier((1, 3, 6, 1, 4, 1, 384, 1, 1))
dnms = MibIdentifier((1, 3, 6, 1, 4, 1, 384, 1, 2))
dynaCommGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 384, 2))
dynaCommDoc = MibIdentifier((1, 3, 6, 1, 4, 1, 384, 3))
mibBuilder.exportSymbols("DYNATECHCOMMUNICATIONS-MIB", dynaCommGeneral=dynaCommGeneral, dnms=dnms, cpx=cpx, dynatechCommunications=dynatechCommunications, dynaCommDoc=dynaCommDoc, dynaCommProducts=dynaCommProducts)
