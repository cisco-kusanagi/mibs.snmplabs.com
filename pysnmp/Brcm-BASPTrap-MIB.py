#
# PySNMP MIB module Brcm-BASPTrap-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Brcm-BASPTrap-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:25:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Counter64, NotificationType, ModuleIdentity, Gauge32, MibIdentifier, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Unsigned32, IpAddress, Bits, iso, TimeTicks, enterprises, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter64", "NotificationType", "ModuleIdentity", "Gauge32", "MibIdentifier", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Unsigned32", "IpAddress", "Bits", "iso", "TimeTicks", "enterprises", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
broadcom = MibIdentifier((1, 3, 6, 1, 4, 1, 4413))
enet = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1))
basp = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 2))
baspConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 2, 1))
baspStat = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 2, 2))
baspTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 2, 3))
trapAdapterName = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 2, 3, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapAdapterName.setStatus('mandatory')
trapTeamName = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 2, 3, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapTeamName.setStatus('mandatory')
trapCauseDirection = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 2, 3, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("adapterActive", 1), ("adapterInactive", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapCauseDirection.setStatus('mandatory')
trapAdapterActivityCause = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 2, 3, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("linkChange", 2), ("adapterEnabledOrDisabled", 3), ("adapterAddedOrRemoved", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapAdapterActivityCause.setStatus('mandatory')
failoverEvent = NotificationType((1, 3, 6, 1, 4, 1, 4413, 1, 2, 3) + (0,1)).setObjects(("Brcm-BASPTrap-MIB", "trapAdapterName"), ("Brcm-BASPTrap-MIB", "trapTeamName"), ("Brcm-BASPTrap-MIB", "trapCauseDirection"), ("Brcm-BASPTrap-MIB", "trapAdapterActivityCause"))
mibBuilder.exportSymbols("Brcm-BASPTrap-MIB", broadcom=broadcom, basp=basp, trapAdapterName=trapAdapterName, failoverEvent=failoverEvent, trapCauseDirection=trapCauseDirection, enet=enet, trapAdapterActivityCause=trapAdapterActivityCause, baspStat=baspStat, baspTrap=baspTrap, trapTeamName=trapTeamName, baspConfig=baspConfig)
