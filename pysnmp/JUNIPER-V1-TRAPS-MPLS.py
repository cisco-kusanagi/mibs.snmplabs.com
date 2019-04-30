#
# PySNMP MIB module JUNIPER-V1-TRAPS-MPLS (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-V1-TRAPS-MPLS
# Produced by pysmi-0.3.4 at Mon Apr 29 19:50:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, Counter64, Integer32, TimeTicks, ModuleIdentity, IpAddress, Bits, iso, MibIdentifier, Unsigned32, ObjectIdentity, Counter32, NotificationType, Gauge32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "Counter64", "Integer32", "TimeTicks", "ModuleIdentity", "IpAddress", "Bits", "iso", "MibIdentifier", "Unsigned32", "ObjectIdentity", "Counter32", "NotificationType", "Gauge32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniperMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 2636))
jnxMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3))
mpls = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 2))
mplsLspList = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3))
mplsLspEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1))
mplsLspName = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 1))
mplsPathName = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 17))
mplsLspUpV1 = NotificationType((1, 3, 6, 1, 4, 1, 2636) + (0,1)).setObjects(("JUNIPER-V1-TRAPS-MPLS", "mplsLspName"), ("JUNIPER-V1-TRAPS-MPLS", "mplsPathName"))
mplsLspDownV1 = NotificationType((1, 3, 6, 1, 4, 1, 2636) + (0,2)).setObjects(("JUNIPER-V1-TRAPS-MPLS", "mplsLspName"), ("JUNIPER-V1-TRAPS-MPLS", "mplsPathName"))
mplsLspChangeV1 = NotificationType((1, 3, 6, 1, 4, 1, 2636) + (0,3)).setObjects(("JUNIPER-V1-TRAPS-MPLS", "mplsLspName"), ("JUNIPER-V1-TRAPS-MPLS", "mplsPathName"))
mibBuilder.exportSymbols("JUNIPER-V1-TRAPS-MPLS", mplsLspName=mplsLspName, mplsLspUpV1=mplsLspUpV1, mplsPathName=mplsPathName, jnxMibs=jnxMibs, mplsLspEntry=mplsLspEntry, mplsLspList=mplsLspList, mplsLspDownV1=mplsLspDownV1, mplsLspChangeV1=mplsLspChangeV1, juniperMIB=juniperMIB, mpls=mpls)
