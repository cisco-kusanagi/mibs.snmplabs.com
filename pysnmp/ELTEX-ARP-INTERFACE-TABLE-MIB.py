#
# PySNMP MIB module ELTEX-ARP-INTERFACE-TABLE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEX-ARP-INTERFACE-TABLE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:45:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
eltMesArpSpec, = mibBuilder.importSymbols("ELTEX-MES-IP", "eltMesArpSpec")
rsArpInterfaceEntry, = mibBuilder.importSymbols("RADLAN-IP", "rsArpInterfaceEntry")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ModuleIdentity, iso, Integer32, MibIdentifier, Unsigned32, Counter64, NotificationType, Gauge32, Bits, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ModuleIdentity", "iso", "Integer32", "MibIdentifier", "Unsigned32", "Counter64", "NotificationType", "Gauge32", "Bits", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
eltArpInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 3, 1), )
if mibBuilder.loadTexts: eltArpInterfaceTable.setStatus('current')
eltArpInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 3, 1, 1), )
rsArpInterfaceEntry.registerAugmentions(("ELTEX-ARP-INTERFACE-TABLE-MIB", "eltArpInterfaceEntry"))
eltArpInterfaceEntry.setIndexNames(*rsArpInterfaceEntry.getIndexNames())
if mibBuilder.loadTexts: eltArpInterfaceEntry.setStatus('current')
eltArpInterfaceArpLocalProxy = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltArpInterfaceArpLocalProxy.setStatus('current')
mibBuilder.exportSymbols("ELTEX-ARP-INTERFACE-TABLE-MIB", eltArpInterfaceEntry=eltArpInterfaceEntry, eltArpInterfaceArpLocalProxy=eltArpInterfaceArpLocalProxy, eltArpInterfaceTable=eltArpInterfaceTable)
