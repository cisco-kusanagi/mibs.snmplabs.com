#
# PySNMP MIB module NETBOTZ-PRD-CRL-MIB2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NETBOTZ-PRD-CRL-MIB2-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:08:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
netBotz_prd_crawlers, = mibBuilder.importSymbols("NETBOTZ-PRODUCTS-MIB", "netBotz-prd-crawlers")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Integer32, Unsigned32, ModuleIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, TimeTicks, iso, Gauge32, IpAddress, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Unsigned32", "ModuleIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "TimeTicks", "iso", "Gauge32", "IpAddress", "MibIdentifier", "Counter32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
netbotz_crawlers = MibIdentifier((1, 3, 6, 1, 4, 1, 5528, 30, 20, 5528)).setLabel("netbotz-crawlers")
netBotz_prd_crl_mib2 = MibIdentifier((1, 3, 6, 1, 4, 1, 5528, 30, 20, 5528, 1)).setLabel("netBotz-prd-crl-mib2")
netBotz_prd_crl_mib2if = MibIdentifier((1, 3, 6, 1, 4, 1, 5528, 30, 20, 5528, 2)).setLabel("netBotz-prd-crl-mib2if")
netBotz_prd_crl_mib2_ping = MibScalar((1, 3, 6, 1, 4, 1, 5528, 30, 20, 5528, 1, 3), Integer32()).setLabel("netBotz-prd-crl-mib2-ping").setMaxAccess("readonly")
if mibBuilder.loadTexts: netBotz_prd_crl_mib2_ping.setStatus('mandatory')
netBotz_prd_crl_mib2_uptime = MibScalar((1, 3, 6, 1, 4, 1, 5528, 30, 20, 5528, 1, 8), TimeTicks()).setLabel("netBotz-prd-crl-mib2-uptime").setMaxAccess("readonly")
if mibBuilder.loadTexts: netBotz_prd_crl_mib2_uptime.setStatus('mandatory')
netBotz_prd_crl_mib2_snmpstatus = MibScalar((1, 3, 6, 1, 4, 1, 5528, 30, 20, 5528, 1, 9), DisplayString()).setLabel("netBotz-prd-crl-mib2-snmpstatus").setMaxAccess("readonly")
if mibBuilder.loadTexts: netBotz_prd_crl_mib2_snmpstatus.setStatus('mandatory')
netBotz_prd_crl_mib2if_opstatus = MibScalar((1, 3, 6, 1, 4, 1, 5528, 30, 20, 5528, 2, 6), Integer32()).setLabel("netBotz-prd-crl-mib2if-opstatus").setMaxAccess("readonly")
if mibBuilder.loadTexts: netBotz_prd_crl_mib2if_opstatus.setStatus('mandatory')
mibBuilder.exportSymbols("NETBOTZ-PRD-CRL-MIB2-MIB", netBotz_prd_crl_mib2_snmpstatus=netBotz_prd_crl_mib2_snmpstatus, netBotz_prd_crl_mib2_uptime=netBotz_prd_crl_mib2_uptime, netBotz_prd_crl_mib2_ping=netBotz_prd_crl_mib2_ping, netBotz_prd_crl_mib2if_opstatus=netBotz_prd_crl_mib2if_opstatus, netbotz_crawlers=netbotz_crawlers, netBotz_prd_crl_mib2=netBotz_prd_crl_mib2, netBotz_prd_crl_mib2if=netBotz_prd_crl_mib2if)
