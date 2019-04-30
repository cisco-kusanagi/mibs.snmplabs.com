#
# PySNMP MIB module QLGC-QLASPTrap-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/QLGC-QLASPTrap-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:35:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, ModuleIdentity, MibIdentifier, Bits, Unsigned32, iso, Gauge32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, Integer32, Counter64, NotificationType, ObjectIdentity, IpAddress, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ModuleIdentity", "MibIdentifier", "Bits", "Unsigned32", "iso", "Gauge32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "Integer32", "Counter64", "NotificationType", "ObjectIdentity", "IpAddress", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
qlogic = MibIdentifier((1, 3, 6, 1, 4, 1, 3873))
enet = MibIdentifier((1, 3, 6, 1, 4, 1, 3873, 1))
qlasp = MibIdentifier((1, 3, 6, 1, 4, 1, 3873, 1, 2))
qlaspConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 3873, 1, 2, 1))
qlaspStat = MibIdentifier((1, 3, 6, 1, 4, 1, 3873, 1, 2, 2))
qlaspTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 3873, 1, 2, 3))
trapAdapterName = MibScalar((1, 3, 6, 1, 4, 1, 3873, 1, 2, 3, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapAdapterName.setStatus('mandatory')
trapTeamName = MibScalar((1, 3, 6, 1, 4, 1, 3873, 1, 2, 3, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapTeamName.setStatus('mandatory')
trapCauseDirection = MibScalar((1, 3, 6, 1, 4, 1, 3873, 1, 2, 3, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("adapterActive", 1), ("adapterInactive", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapCauseDirection.setStatus('mandatory')
trapAdapterActivityCause = MibScalar((1, 3, 6, 1, 4, 1, 3873, 1, 2, 3, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("linkChange", 2), ("adapterEnabledOrDisabled", 3), ("adapterAddedOrRemoved", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapAdapterActivityCause.setStatus('mandatory')
failoverEvent = NotificationType((1, 3, 6, 1, 4, 1, 3873, 1, 2, 3) + (0,1)).setObjects(("QLGC-QLASPTrap-MIB", "trapAdapterName"), ("QLGC-QLASPTrap-MIB", "trapTeamName"), ("QLGC-QLASPTrap-MIB", "trapCauseDirection"), ("QLGC-QLASPTrap-MIB", "trapAdapterActivityCause"))
mibBuilder.exportSymbols("QLGC-QLASPTrap-MIB", trapAdapterActivityCause=trapAdapterActivityCause, qlasp=qlasp, enet=enet, qlaspConfig=qlaspConfig, trapAdapterName=trapAdapterName, qlaspStat=qlaspStat, qlogic=qlogic, qlaspTrap=qlaspTrap, trapCauseDirection=trapCauseDirection, trapTeamName=trapTeamName, failoverEvent=failoverEvent)
