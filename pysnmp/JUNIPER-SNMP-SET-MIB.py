#
# PySNMP MIB module JUNIPER-SNMP-SET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-SNMP-SET-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:50:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
jnxSnmpSetTraps, jnxSnmpSetMibRoot = mibBuilder.importSymbols("JUNIPER-SMI", "jnxSnmpSetTraps", "jnxSnmpSetMibRoot")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter64, Counter32, NotificationType, IpAddress, Bits, MibIdentifier, ObjectIdentity, Gauge32, TimeTicks, iso, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter64", "Counter32", "NotificationType", "IpAddress", "Bits", "MibIdentifier", "ObjectIdentity", "Gauge32", "TimeTicks", "iso", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
jnxSnmpSetMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 76, 1))
jnxSnmpSetMib.setRevisions(('2013-11-26 00:00',))
if mibBuilder.loadTexts: jnxSnmpSetMib.setLastUpdated('201201271000Z')
if mibBuilder.loadTexts: jnxSnmpSetMib.setOrganization('Juniper Networks, Inc.')
jnxSnmpSet = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 76, 1, 1))
jnxSnmpSetNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 4, 24, 1))
jnxCommitSetFailureReason = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 76, 1, 1, 1), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxCommitSetFailureReason.setStatus('current')
jnxSnmpSetFailure = NotificationType((1, 3, 6, 1, 4, 1, 2636, 4, 24, 1, 1)).setObjects(("JUNIPER-SNMP-SET-MIB", "jnxCommitSetFailureReason"))
if mibBuilder.loadTexts: jnxSnmpSetFailure.setStatus('current')
mibBuilder.exportSymbols("JUNIPER-SNMP-SET-MIB", jnxSnmpSetMib=jnxSnmpSetMib, jnxSnmpSetNotifications=jnxSnmpSetNotifications, jnxSnmpSet=jnxSnmpSet, PYSNMP_MODULE_ID=jnxSnmpSetMib, jnxSnmpSetFailure=jnxSnmpSetFailure, jnxCommitSetFailureReason=jnxCommitSetFailureReason)
