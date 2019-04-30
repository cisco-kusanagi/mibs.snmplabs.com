#
# PySNMP MIB module BEKARTS-v1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BEKARTS-v1-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:20:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Unsigned32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, enterprises, Integer32, NotificationType, Counter32, NotificationType, Counter64, IpAddress, MibIdentifier, Gauge32, iso, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "enterprises", "Integer32", "NotificationType", "Counter32", "NotificationType", "Counter64", "IpAddress", "MibIdentifier", "Gauge32", "iso", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
bekarts = MibIdentifier((1, 3, 6, 1, 4, 1, 18514))
bekarts_software = MibIdentifier((1, 3, 6, 1, 4, 1, 18514, 20)).setLabel("bekarts-software")
bekarts_hardware = MibIdentifier((1, 3, 6, 1, 4, 1, 18514, 100)).setLabel("bekarts-hardware")
bekarts_mailshappy = MibIdentifier((1, 3, 6, 1, 4, 1, 18514, 20, 1)).setLabel("bekarts-mailshappy")
bekarts_mailshappy_on = NotificationType((1, 3, 6, 1, 4, 1, 18514, 20, 1) + (0,1)).setLabel("bekarts-mailshappy-on")
bekarts_mailshappy_off = NotificationType((1, 3, 6, 1, 4, 1, 18514, 20, 1) + (0,2)).setLabel("bekarts-mailshappy-off")
bekarts_mailshappy_active = NotificationType((1, 3, 6, 1, 4, 1, 18514, 20, 1) + (0,3)).setLabel("bekarts-mailshappy-active")
bekarts_mailshappy_deactive = NotificationType((1, 3, 6, 1, 4, 1, 18514, 20, 1) + (0,4)).setLabel("bekarts-mailshappy-deactive")
bekarts_mailshappy_warning = NotificationType((1, 3, 6, 1, 4, 1, 18514, 20, 1) + (0,5)).setLabel("bekarts-mailshappy-warning")
bekarts_mailshappy_clear_warning = NotificationType((1, 3, 6, 1, 4, 1, 18514, 20, 1) + (0,6)).setLabel("bekarts-mailshappy-clear-warning")
bekarts_mailshappy_critical = NotificationType((1, 3, 6, 1, 4, 1, 18514, 20, 1) + (0,7)).setLabel("bekarts-mailshappy-critical")
bekarts_mailshappy_clear_critical = NotificationType((1, 3, 6, 1, 4, 1, 18514, 20, 1) + (0,8)).setLabel("bekarts-mailshappy-clear-critical")
bekarts_mailshappy_test = NotificationType((1, 3, 6, 1, 4, 1, 18514, 20, 1) + (0,9)).setLabel("bekarts-mailshappy-test")
mibBuilder.exportSymbols("BEKARTS-v1-MIB", bekarts_software=bekarts_software, bekarts_mailshappy_active=bekarts_mailshappy_active, bekarts_mailshappy_critical=bekarts_mailshappy_critical, bekarts_mailshappy_deactive=bekarts_mailshappy_deactive, bekarts_mailshappy_warning=bekarts_mailshappy_warning, bekarts_mailshappy_test=bekarts_mailshappy_test, bekarts_mailshappy_clear_warning=bekarts_mailshappy_clear_warning, bekarts_mailshappy=bekarts_mailshappy, bekarts_hardware=bekarts_hardware, bekarts_mailshappy_on=bekarts_mailshappy_on, bekarts=bekarts, bekarts_mailshappy_clear_critical=bekarts_mailshappy_clear_critical, bekarts_mailshappy_off=bekarts_mailshappy_off)
