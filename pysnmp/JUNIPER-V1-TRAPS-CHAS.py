#
# PySNMP MIB module JUNIPER-V1-TRAPS-CHAS (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-V1-TRAPS-CHAS
# Produced by pysmi-0.3.4 at Mon Apr 29 19:50:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, NotificationType, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ObjectIdentity, ModuleIdentity, IpAddress, MibIdentifier, Unsigned32, Counter32, Counter64, Integer32, Gauge32, enterprises, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ObjectIdentity", "ModuleIdentity", "IpAddress", "MibIdentifier", "Unsigned32", "Counter32", "Counter64", "Integer32", "Gauge32", "enterprises", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniperMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 2636))
jnxMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3))
jnxBoxAnatomy = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 1))
jnxContentsTable = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 1, 8))
jnxContentsEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 1, 8, 1))
jnxContentsContainerIndex = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 1, 8, 1, 1))
jnxContentsL1Index = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 1, 8, 1, 2))
jnxContentsL2Index = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 1, 8, 1, 3))
jnxContentsL3Index = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 1, 8, 1, 4))
jnxContentsDescr = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 1, 8, 1, 6))
jnxPowerSupplyFailureV1 = NotificationType((1, 3, 6, 1, 4, 1, 2636) + (0,1)).setObjects(("JUNIPER-V1-TRAPS-CHAS", "jnxContentsContainerIndex"), ("JUNIPER-V1-TRAPS-CHAS", "jnxContentsL1Index"), ("JUNIPER-V1-TRAPS-CHAS", "jnxContentsL2Index"), ("JUNIPER-V1-TRAPS-CHAS", "jnxContentsL3Index"), ("JUNIPER-V1-TRAPS-CHAS", "jnxContentsDescr"))
jnxFanFailureV1 = NotificationType((1, 3, 6, 1, 4, 1, 2636) + (0,2)).setObjects(("JUNIPER-V1-TRAPS-CHAS", "jnxContentsContainerIndex"), ("JUNIPER-V1-TRAPS-CHAS", "jnxContentsL1Index"), ("JUNIPER-V1-TRAPS-CHAS", "jnxContentsL2Index"), ("JUNIPER-V1-TRAPS-CHAS", "jnxContentsL3Index"), ("JUNIPER-V1-TRAPS-CHAS", "jnxContentsDescr"))
jnxOverTemperatureV1 = NotificationType((1, 3, 6, 1, 4, 1, 2636) + (0,3)).setObjects(("JUNIPER-V1-TRAPS-CHAS", "jnxContentsContainerIndex"), ("JUNIPER-V1-TRAPS-CHAS", "jnxContentsL1Index"), ("JUNIPER-V1-TRAPS-CHAS", "jnxContentsL2Index"), ("JUNIPER-V1-TRAPS-CHAS", "jnxContentsL3Index"), ("JUNIPER-V1-TRAPS-CHAS", "jnxContentsDescr"))
mibBuilder.exportSymbols("JUNIPER-V1-TRAPS-CHAS", jnxContentsDescr=jnxContentsDescr, jnxPowerSupplyFailureV1=jnxPowerSupplyFailureV1, jnxMibs=jnxMibs, jnxBoxAnatomy=jnxBoxAnatomy, jnxOverTemperatureV1=jnxOverTemperatureV1, jnxContentsEntry=jnxContentsEntry, jnxContentsContainerIndex=jnxContentsContainerIndex, jnxContentsL1Index=jnxContentsL1Index, jnxFanFailureV1=jnxFanFailureV1, jnxContentsTable=jnxContentsTable, juniperMIB=juniperMIB, jnxContentsL2Index=jnxContentsL2Index, jnxContentsL3Index=jnxContentsL3Index)
