#
# PySNMP MIB module DYNATECHCOMMUNICATIONS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DYNATECHCOMMUNICATIONS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:36:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, IpAddress, ModuleIdentity, enterprises, MibIdentifier, Unsigned32, Bits, TimeTicks, Counter32, Gauge32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "IpAddress", "ModuleIdentity", "enterprises", "MibIdentifier", "Unsigned32", "Bits", "TimeTicks", "Counter32", "Gauge32", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
dynatechCommunications = MibIdentifier((1, 3, 6, 1, 4, 1, 384))
dynaCommProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 384, 1))
cpx = MibIdentifier((1, 3, 6, 1, 4, 1, 384, 1, 1))
dnms = MibIdentifier((1, 3, 6, 1, 4, 1, 384, 1, 2))
dynaCommGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 384, 2))
dynaCommDoc = MibIdentifier((1, 3, 6, 1, 4, 1, 384, 3))
mibBuilder.exportSymbols("DYNATECHCOMMUNICATIONS-MIB", dynaCommDoc=dynaCommDoc, cpx=cpx, dynatechCommunications=dynatechCommunications, dynaCommProducts=dynaCommProducts, dnms=dnms, dynaCommGeneral=dynaCommGeneral)
