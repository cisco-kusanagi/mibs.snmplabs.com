#
# PySNMP MIB module ELTEX-ARP-INTERFACE-TABLE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEX-ARP-INTERFACE-TABLE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:00:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
eltMesArpSpec, = mibBuilder.importSymbols("ELTEX-MES-IP", "eltMesArpSpec")
rsArpInterfaceEntry, = mibBuilder.importSymbols("RADLAN-IP", "rsArpInterfaceEntry")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter64, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, NotificationType, MibIdentifier, Gauge32, IpAddress, Counter32, TimeTicks, Unsigned32, ObjectIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "NotificationType", "MibIdentifier", "Gauge32", "IpAddress", "Counter32", "TimeTicks", "Unsigned32", "ObjectIdentity", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
eltArpInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 3, 1), )
if mibBuilder.loadTexts: eltArpInterfaceTable.setStatus('current')
if mibBuilder.loadTexts: eltArpInterfaceTable.setDescription('')
eltArpInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 3, 1, 1), )
rsArpInterfaceEntry.registerAugmentions(("ELTEX-ARP-INTERFACE-TABLE-MIB", "eltArpInterfaceEntry"))
eltArpInterfaceEntry.setIndexNames(*rsArpInterfaceEntry.getIndexNames())
if mibBuilder.loadTexts: eltArpInterfaceEntry.setStatus('current')
if mibBuilder.loadTexts: eltArpInterfaceEntry.setDescription('Each entry contains L2 Interface specific configuration for ARP Application.')
eltArpInterfaceArpLocalProxy = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltArpInterfaceArpLocalProxy.setStatus('current')
if mibBuilder.loadTexts: eltArpInterfaceArpLocalProxy.setDescription('When Local ARP Proxy is enabled, the router can respond to ARP requests for nodes located on a same sub-net, provided they are it its network table. The router responds with its own MAC address. When ARP Proxy is disabled, the router responds only to ARP requests for its own IP addresses.')
mibBuilder.exportSymbols("ELTEX-ARP-INTERFACE-TABLE-MIB", eltArpInterfaceEntry=eltArpInterfaceEntry, eltArpInterfaceArpLocalProxy=eltArpInterfaceArpLocalProxy, eltArpInterfaceTable=eltArpInterfaceTable)
