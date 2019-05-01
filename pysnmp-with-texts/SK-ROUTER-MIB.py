#
# PySNMP MIB module SK-ROUTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SK-ROUTER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:04:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
DisplayString, = mibBuilder.importSymbols("RFC1155-SMI", "DisplayString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, IpAddress, NotificationType, Gauge32, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, MibIdentifier, Counter32, ModuleIdentity, Bits, Counter64, Unsigned32, TimeTicks, Integer32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "IpAddress", "NotificationType", "Gauge32", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "MibIdentifier", "Counter32", "ModuleIdentity", "Bits", "Counter64", "Unsigned32", "TimeTicks", "Integer32", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
sk = MibIdentifier((1, 3, 6, 1, 4, 1, 179))
skSystems = MibIdentifier((1, 3, 6, 1, 4, 1, 179, 1))
skMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 179, 2))
skRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 179, 1, 1))
skConcentrator = MibIdentifier((1, 3, 6, 1, 4, 1, 179, 1, 2))
skSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 179, 1, 3))
skDLI = MibIdentifier((1, 3, 6, 1, 4, 1, 179, 2, 1))
mibBuilder.exportSymbols("SK-ROUTER-MIB", skMibs=skMibs, sk=sk, skSwitch=skSwitch, skDLI=skDLI, skConcentrator=skConcentrator, skSystems=skSystems, skRouter=skRouter)
