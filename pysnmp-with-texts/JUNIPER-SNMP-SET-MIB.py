#
# PySNMP MIB module JUNIPER-SNMP-SET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-SNMP-SET-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:01:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
jnxSnmpSetMibRoot, jnxSnmpSetTraps = mibBuilder.importSymbols("JUNIPER-SMI", "jnxSnmpSetMibRoot", "jnxSnmpSetTraps")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Integer32, TimeTicks, Bits, ObjectIdentity, Counter32, IpAddress, NotificationType, Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Gauge32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Integer32", "TimeTicks", "Bits", "ObjectIdentity", "Counter32", "IpAddress", "NotificationType", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Gauge32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
jnxSnmpSetMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 76, 1))
jnxSnmpSetMib.setRevisions(('2013-11-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: jnxSnmpSetMib.setRevisionsDescriptions(('Added General trap for SNMP set failure.',))
if mibBuilder.loadTexts: jnxSnmpSetMib.setLastUpdated('201201271000Z')
if mibBuilder.loadTexts: jnxSnmpSetMib.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: jnxSnmpSetMib.setContactInfo(' Juniper Technical Assistance Center Juniper Networks, Inc. 1194 N. Mathilda Avenue Sunnyvale, CA 94089 E-mail: support@juniper.net')
if mibBuilder.loadTexts: jnxSnmpSetMib.setDescription('This MIB module defines objects used for managing SNMP sets for Juniper products.')
jnxSnmpSet = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 76, 1, 1))
jnxSnmpSetNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 4, 24, 1))
jnxCommitSetFailureReason = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 76, 1, 1, 1), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxCommitSetFailureReason.setStatus('current')
if mibBuilder.loadTexts: jnxCommitSetFailureReason.setDescription(' This is the reason for the failure ... Text information about the failure ')
jnxSnmpSetFailure = NotificationType((1, 3, 6, 1, 4, 1, 2636, 4, 24, 1, 1)).setObjects(("JUNIPER-SNMP-SET-MIB", "jnxCommitSetFailureReason"))
if mibBuilder.loadTexts: jnxSnmpSetFailure.setStatus('current')
if mibBuilder.loadTexts: jnxSnmpSetFailure.setDescription('Notification for a snmp set commit error.')
mibBuilder.exportSymbols("JUNIPER-SNMP-SET-MIB", jnxSnmpSetMib=jnxSnmpSetMib, jnxSnmpSetNotifications=jnxSnmpSetNotifications, jnxSnmpSet=jnxSnmpSet, jnxSnmpSetFailure=jnxSnmpSetFailure, jnxCommitSetFailureReason=jnxCommitSetFailureReason, PYSNMP_MODULE_ID=jnxSnmpSetMib)
