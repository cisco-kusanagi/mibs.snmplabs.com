#
# PySNMP MIB module JUNIPER-V1-TRAPS-MPLS (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-V1-TRAPS-MPLS
# Produced by pysmi-0.3.4 at Wed May  1 14:01:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, iso, IpAddress, Bits, ModuleIdentity, Counter32, NotificationType, Gauge32, ObjectIdentity, NotificationType, Unsigned32, Integer32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "iso", "IpAddress", "Bits", "ModuleIdentity", "Counter32", "NotificationType", "Gauge32", "ObjectIdentity", "NotificationType", "Unsigned32", "Integer32", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniperMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 2636))
jnxMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3))
mpls = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 2))
mplsLspList = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3))
mplsLspEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1))
mplsLspName = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 1))
mplsPathName = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 17))
mplsLspUpV1 = NotificationType((1, 3, 6, 1, 4, 1, 2636) + (0,1)).setObjects(("JUNIPER-V1-TRAPS-MPLS", "mplsLspName"), ("JUNIPER-V1-TRAPS-MPLS", "mplsPathName"))
if mibBuilder.loadTexts: mplsLspUpV1.setDescription('An mplsLspUp trap signifies that the specified LSP is up. The current active path for the LSP is mplsPathName.')
mplsLspDownV1 = NotificationType((1, 3, 6, 1, 4, 1, 2636) + (0,2)).setObjects(("JUNIPER-V1-TRAPS-MPLS", "mplsLspName"), ("JUNIPER-V1-TRAPS-MPLS", "mplsPathName"))
if mibBuilder.loadTexts: mplsLspDownV1.setDescription('An mplsLspDown trap signifies that the specified LSP is down, because the current active path mplsPathName went down.')
mplsLspChangeV1 = NotificationType((1, 3, 6, 1, 4, 1, 2636) + (0,3)).setObjects(("JUNIPER-V1-TRAPS-MPLS", "mplsLspName"), ("JUNIPER-V1-TRAPS-MPLS", "mplsPathName"))
if mibBuilder.loadTexts: mplsLspChangeV1.setDescription("An mplsLspChange trap signifies that the the specified LSP has switched traffic to the new active path 'toLspPath'. The LSP maintains up state before and after the switch over")
mibBuilder.exportSymbols("JUNIPER-V1-TRAPS-MPLS", mpls=mpls, mplsLspChangeV1=mplsLspChangeV1, mplsLspName=mplsLspName, mplsPathName=mplsPathName, mplsLspUpV1=mplsLspUpV1, mplsLspEntry=mplsLspEntry, jnxMibs=jnxMibs, mplsLspDownV1=mplsLspDownV1, juniperMIB=juniperMIB, mplsLspList=mplsLspList)
