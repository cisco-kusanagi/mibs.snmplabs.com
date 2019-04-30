#
# PySNMP MIB module JUNIPER-EVENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-EVENT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:48:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
jnxEventNotifications, jnxMibs = mibBuilder.importSymbols("JUNIPER-SMI", "jnxEventNotifications", "jnxMibs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, TimeTicks, NotificationType, IpAddress, Unsigned32, iso, Counter32, Gauge32, ModuleIdentity, MibIdentifier, Integer32, Counter64, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "TimeTicks", "NotificationType", "IpAddress", "Unsigned32", "iso", "Counter32", "Gauge32", "ModuleIdentity", "MibIdentifier", "Integer32", "Counter64", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
jnxEvent = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 37))
jnxEvent.setRevisions(('2006-08-16 21:53',))
if mibBuilder.loadTexts: jnxEvent.setLastUpdated('200608162153Z')
if mibBuilder.loadTexts: jnxEvent.setOrganization('Juniper Networks, Inc.')
jnxEventNotifyVars = ObjectIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 37, 1))
if mibBuilder.loadTexts: jnxEventNotifyVars.setStatus('current')
jnxEventTrapDescr = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 37, 1, 1), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxEventTrapDescr.setStatus('current')
jnxEventAvTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 37, 1, 2), )
if mibBuilder.loadTexts: jnxEventAvTable.setStatus('current')
jnxEventAvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 37, 1, 2, 1), ).setIndexNames((0, "JUNIPER-EVENT-MIB", "jnxEventAvIndex"))
if mibBuilder.loadTexts: jnxEventAvEntry.setStatus('current')
jnxEventAvIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 37, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: jnxEventAvIndex.setStatus('current')
jnxEventAvAttribute = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 37, 1, 2, 1, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxEventAvAttribute.setStatus('current')
jnxEventAvValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 37, 1, 2, 1, 3), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxEventAvValue.setStatus('current')
jnxEventNotificationPrefix = ObjectIdentity((1, 3, 6, 1, 4, 1, 2636, 4, 13, 0))
if mibBuilder.loadTexts: jnxEventNotificationPrefix.setStatus('current')
jnxEventTrap = NotificationType((1, 3, 6, 1, 4, 1, 2636, 4, 13, 0, 1)).setObjects(("JUNIPER-EVENT-MIB", "jnxEventTrapDescr"))
if mibBuilder.loadTexts: jnxEventTrap.setStatus('current')
mibBuilder.exportSymbols("JUNIPER-EVENT-MIB", jnxEventNotifyVars=jnxEventNotifyVars, PYSNMP_MODULE_ID=jnxEvent, jnxEventTrapDescr=jnxEventTrapDescr, jnxEventAvAttribute=jnxEventAvAttribute, jnxEventTrap=jnxEventTrap, jnxEvent=jnxEvent, jnxEventAvTable=jnxEventAvTable, jnxEventAvValue=jnxEventAvValue, jnxEventNotificationPrefix=jnxEventNotificationPrefix, jnxEventAvIndex=jnxEventAvIndex, jnxEventAvEntry=jnxEventAvEntry)