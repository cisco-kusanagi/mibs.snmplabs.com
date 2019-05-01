#
# PySNMP MIB module NETBOTZ-SNMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NETBOTZ-SNMP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:18:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
netBotz_snmp, = mibBuilder.importSymbols("NETBOTZ-MIB", "netBotz-snmp")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, iso, NotificationType, ObjectIdentity, TimeTicks, Gauge32, Counter32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Bits, Integer32, MibIdentifier, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "iso", "NotificationType", "ObjectIdentity", "TimeTicks", "Gauge32", "Counter32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Bits", "Integer32", "MibIdentifier", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
netBotz_snmp_traptarget = MibScalar((1, 3, 6, 1, 4, 1, 5528, 40, 1), IpAddress()).setLabel("netBotz-snmp-traptarget").setMaxAccess("readwrite")
if mibBuilder.loadTexts: netBotz_snmp_traptarget.setReference('Netbotz Trap Target')
if mibBuilder.loadTexts: netBotz_snmp_traptarget.setStatus('mandatory')
if mibBuilder.loadTexts: netBotz_snmp_traptarget.setDescription('Target of traps from the Netbotz device. This field contains the IP address where Netbotz traps are to be sent.')
netBotz_snmp_community = MibScalar((1, 3, 6, 1, 4, 1, 5528, 40, 2), DisplayString()).setLabel("netBotz-snmp-community").setMaxAccess("readwrite")
if mibBuilder.loadTexts: netBotz_snmp_community.setReference('Read/Write Community')
if mibBuilder.loadTexts: netBotz_snmp_community.setStatus('mandatory')
if mibBuilder.loadTexts: netBotz_snmp_community.setDescription('The read/write community of the Netbotz device.')
netBotz_snmp_timeout = MibScalar((1, 3, 6, 1, 4, 1, 5528, 40, 3), Integer32()).setLabel("netBotz-snmp-timeout").setMaxAccess("readwrite")
if mibBuilder.loadTexts: netBotz_snmp_timeout.setReference('SNMP Timeout')
if mibBuilder.loadTexts: netBotz_snmp_timeout.setStatus('mandatory')
if mibBuilder.loadTexts: netBotz_snmp_timeout.setDescription('SNMP Timeout period.')
netBotz_snmp_retries = MibScalar((1, 3, 6, 1, 4, 1, 5528, 40, 4), Integer32()).setLabel("netBotz-snmp-retries").setMaxAccess("readwrite")
if mibBuilder.loadTexts: netBotz_snmp_retries.setReference('SNMP Retries')
if mibBuilder.loadTexts: netBotz_snmp_retries.setStatus('mandatory')
if mibBuilder.loadTexts: netBotz_snmp_retries.setDescription('SNMP Retry count.')
netBotz_userid_1 = MibScalar((1, 3, 6, 1, 4, 1, 5528, 40, 5), DisplayString()).setLabel("netBotz-userid-1").setMaxAccess("readwrite")
if mibBuilder.loadTexts: netBotz_userid_1.setReference('UserID 1')
if mibBuilder.loadTexts: netBotz_userid_1.setStatus('mandatory')
if mibBuilder.loadTexts: netBotz_userid_1.setDescription('The userID of the supervisor account (write-only).')
netBotz_password_1 = MibScalar((1, 3, 6, 1, 4, 1, 5528, 40, 6), DisplayString()).setLabel("netBotz-password-1").setMaxAccess("readwrite")
if mibBuilder.loadTexts: netBotz_password_1.setReference('Password 1')
if mibBuilder.loadTexts: netBotz_password_1.setStatus('mandatory')
if mibBuilder.loadTexts: netBotz_password_1.setDescription('The password of the supervisor account (write-only).')
netBotz_userid_2 = MibScalar((1, 3, 6, 1, 4, 1, 5528, 40, 7), DisplayString()).setLabel("netBotz-userid-2").setMaxAccess("readwrite")
if mibBuilder.loadTexts: netBotz_userid_2.setReference('UserID 2')
if mibBuilder.loadTexts: netBotz_userid_2.setStatus('mandatory')
if mibBuilder.loadTexts: netBotz_userid_2.setDescription('The userID of the full read access account (write-only).')
netBotz_password_2 = MibScalar((1, 3, 6, 1, 4, 1, 5528, 40, 8), DisplayString()).setLabel("netBotz-password-2").setMaxAccess("readwrite")
if mibBuilder.loadTexts: netBotz_password_2.setReference('Password 2')
if mibBuilder.loadTexts: netBotz_password_2.setStatus('mandatory')
if mibBuilder.loadTexts: netBotz_password_2.setDescription('The password of the full read access account (write-only).')
netBotz_userid_3 = MibScalar((1, 3, 6, 1, 4, 1, 5528, 40, 9), DisplayString()).setLabel("netBotz-userid-3").setMaxAccess("readwrite")
if mibBuilder.loadTexts: netBotz_userid_3.setReference('UserID 3')
if mibBuilder.loadTexts: netBotz_userid_3.setStatus('mandatory')
if mibBuilder.loadTexts: netBotz_userid_3.setDescription('The userID of the minimum read access account (write-only).')
netBotz_password_3 = MibScalar((1, 3, 6, 1, 4, 1, 5528, 40, 10), DisplayString()).setLabel("netBotz-password-3").setMaxAccess("readwrite")
if mibBuilder.loadTexts: netBotz_password_3.setReference('Password 3')
if mibBuilder.loadTexts: netBotz_password_3.setStatus('mandatory')
if mibBuilder.loadTexts: netBotz_password_3.setDescription('The password of the minimum read access account (write-only).')
netBotz_snmp_traptarget2 = MibScalar((1, 3, 6, 1, 4, 1, 5528, 40, 11), IpAddress()).setLabel("netBotz-snmp-traptarget2").setMaxAccess("readwrite")
if mibBuilder.loadTexts: netBotz_snmp_traptarget2.setReference('Netbotz Trap Target 2')
if mibBuilder.loadTexts: netBotz_snmp_traptarget2.setStatus('mandatory')
if mibBuilder.loadTexts: netBotz_snmp_traptarget2.setDescription('Second target of traps from the Netbotz device. This field contains an additional IP address where Netbotz traps are to be sent.')
mibBuilder.exportSymbols("NETBOTZ-SNMP-MIB", netBotz_snmp_retries=netBotz_snmp_retries, netBotz_userid_1=netBotz_userid_1, netBotz_password_2=netBotz_password_2, netBotz_snmp_traptarget=netBotz_snmp_traptarget, netBotz_snmp_traptarget2=netBotz_snmp_traptarget2, netBotz_password_3=netBotz_password_3, netBotz_snmp_timeout=netBotz_snmp_timeout, netBotz_snmp_community=netBotz_snmp_community, netBotz_password_1=netBotz_password_1, netBotz_userid_2=netBotz_userid_2, netBotz_userid_3=netBotz_userid_3)