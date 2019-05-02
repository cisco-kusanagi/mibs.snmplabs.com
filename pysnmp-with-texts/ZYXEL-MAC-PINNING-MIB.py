#
# PySNMP MIB module ZYXEL-MAC-PINNING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-MAC-PINNING-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:50:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
dot1dBasePort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Integer32, Counter32, ModuleIdentity, ObjectIdentity, MibIdentifier, Bits, NotificationType, iso, Counter64, Gauge32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Integer32", "Counter32", "ModuleIdentity", "ObjectIdentity", "MibIdentifier", "Bits", "NotificationType", "iso", "Counter64", "Gauge32", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelMacPinning = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 92))
if mibBuilder.loadTexts: zyxelMacPinning.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelMacPinning.setOrganization('Enterprise Solution ZyXEL')
if mibBuilder.loadTexts: zyxelMacPinning.setContactInfo('')
if mibBuilder.loadTexts: zyxelMacPinning.setDescription('The subtree for MAC Pinning')
zyxelMacPinningSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 92, 1))
zyMacPinningState = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 92, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMacPinningState.setStatus('current')
if mibBuilder.loadTexts: zyMacPinningState.setDescription('Enable/Disable MAC pinning on the switch.')
zyxelMacPinningPortTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 92, 1, 2), )
if mibBuilder.loadTexts: zyxelMacPinningPortTable.setStatus('current')
if mibBuilder.loadTexts: zyxelMacPinningPortTable.setDescription('The table contains MAC pinning port configuration.')
zyxelMacPinningPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 92, 1, 2, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts: zyxelMacPinningPortEntry.setStatus('current')
if mibBuilder.loadTexts: zyxelMacPinningPortEntry.setDescription('An entry contains MAC pinning port configuration.')
zyMacPinningPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 92, 1, 2, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMacPinningPortState.setStatus('current')
if mibBuilder.loadTexts: zyMacPinningPortState.setDescription('Enable/Disable MAC pinning on the port.')
mibBuilder.exportSymbols("ZYXEL-MAC-PINNING-MIB", zyMacPinningState=zyMacPinningState, PYSNMP_MODULE_ID=zyxelMacPinning, zyxelMacPinningPortTable=zyxelMacPinningPortTable, zyxelMacPinning=zyxelMacPinning, zyxelMacPinningPortEntry=zyxelMacPinningPortEntry, zyxelMacPinningSetup=zyxelMacPinningSetup, zyMacPinningPortState=zyMacPinningPortState)
