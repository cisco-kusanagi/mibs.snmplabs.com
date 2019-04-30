#
# PySNMP MIB module Brcm-BSAPTrap-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Brcm-BSAPTrap-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:25:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ModuleIdentity, Unsigned32, MibIdentifier, TimeTicks, enterprises, NotificationType, Bits, Counter64, ObjectIdentity, NotificationType, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ModuleIdentity", "Unsigned32", "MibIdentifier", "TimeTicks", "enterprises", "NotificationType", "Bits", "Counter64", "ObjectIdentity", "NotificationType", "Counter32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
broadcom = MibIdentifier((1, 3, 6, 1, 4, 1, 4413))
enet = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1))
basp = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 2))
baspConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 2, 1))
baspStat = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 2, 2))
baspTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 2, 3))
trapAdapterName = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 2, 3, 1), DisplayString())
if mibBuilder.loadTexts: trapAdapterName.setStatus('mandatory')
trapTeamName = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 2, 3, 2), DisplayString())
if mibBuilder.loadTexts: trapTeamName.setStatus('mandatory')
trapCauseDirection = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 2, 3, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("adapterActive", 1), ("adapterInactive", 2), ("linkup", 3), ("linkdown", 4), ("adapterEnabled", 5), ("adapterDisabled", 6), ("addedToTeam", 7), ("removedFrTeam", 8))))
if mibBuilder.loadTexts: trapCauseDirection.setStatus('mandatory')
trapAdapterActivityCause = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 2, 3, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("linkChange", 2), ("adapterEnabledOrDisabled", 3), ("adapterAddedOrRemoved", 4))))
if mibBuilder.loadTexts: trapAdapterActivityCause.setStatus('mandatory')
failoverEvent = NotificationType((1, 3, 6, 1, 4, 1, 4413, 1, 2, 3) + (0,1)).setObjects(("Brcm-BSAPTrap-MIB", "trapAdapterName"), ("Brcm-BSAPTrap-MIB", "trapTeamName"), ("Brcm-BSAPTrap-MIB", "trapCauseDirection"), ("Brcm-BSAPTrap-MIB", "trapAdapterActivityCause"))
mibBuilder.exportSymbols("Brcm-BSAPTrap-MIB", trapAdapterActivityCause=trapAdapterActivityCause, trapAdapterName=trapAdapterName, trapCauseDirection=trapCauseDirection, baspConfig=baspConfig, basp=basp, broadcom=broadcom, failoverEvent=failoverEvent, baspStat=baspStat, baspTrap=baspTrap, enet=enet, trapTeamName=trapTeamName)
