#
# PySNMP MIB module SK-ROUTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SK-ROUTER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:56:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
DisplayString, = mibBuilder.importSymbols("RFC1155-SMI", "DisplayString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, MibIdentifier, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType, enterprises, Counter64, ModuleIdentity, IpAddress, Gauge32, iso, Counter32, Bits, ObjectIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType", "enterprises", "Counter64", "ModuleIdentity", "IpAddress", "Gauge32", "iso", "Counter32", "Bits", "ObjectIdentity", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
sk = MibIdentifier((1, 3, 6, 1, 4, 1, 179))
skSystems = MibIdentifier((1, 3, 6, 1, 4, 1, 179, 1))
skMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 179, 2))
skRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 179, 1, 1))
skConcentrator = MibIdentifier((1, 3, 6, 1, 4, 1, 179, 1, 2))
skSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 179, 1, 3))
skDLI = MibIdentifier((1, 3, 6, 1, 4, 1, 179, 2, 1))
mibBuilder.exportSymbols("SK-ROUTER-MIB", skSwitch=skSwitch, skDLI=skDLI, skConcentrator=skConcentrator, skRouter=skRouter, skMibs=skMibs, sk=sk, skSystems=skSystems)
