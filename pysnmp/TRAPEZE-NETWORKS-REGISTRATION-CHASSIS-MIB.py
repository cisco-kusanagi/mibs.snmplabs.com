#
# PySNMP MIB module TRAPEZE-NETWORKS-REGISTRATION-CHASSIS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TRAPEZE-NETWORKS-REGISTRATION-CHASSIS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:19:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Counter64, Integer32, Bits, iso, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, MibIdentifier, TimeTicks, ModuleIdentity, NotificationType, IpAddress, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter64", "Integer32", "Bits", "iso", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "MibIdentifier", "TimeTicks", "ModuleIdentity", "NotificationType", "IpAddress", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
trpzRegistration, = mibBuilder.importSymbols("TRAPEZE-NETWORKS-ROOT-MIB", "trpzRegistration")
trpzRegistrationChassisMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 14525, 3, 5))
trpzRegistrationChassisMib.setRevisions(('2007-08-22 00:00',))
if mibBuilder.loadTexts: trpzRegistrationChassisMib.setLastUpdated('200708220000Z')
if mibBuilder.loadTexts: trpzRegistrationChassisMib.setOrganization('Trapeze Networks')
trpzChassisComponents = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 3, 4))
trpzChasCompPowerSupplies = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 3, 4, 1))
trpzChasCompFans = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 3, 4, 2))
trpzChasCompPowerSupply1 = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 3, 4, 1, 1))
trpzChasCompPowerSupply2 = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 3, 4, 1, 2))
trpzChasCompFan1 = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 3, 4, 2, 1))
trpzChasCompFan2 = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 3, 4, 2, 2))
trpzChasCompFan3 = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 3, 4, 2, 3))
mibBuilder.exportSymbols("TRAPEZE-NETWORKS-REGISTRATION-CHASSIS-MIB", trpzChasCompFan2=trpzChasCompFan2, trpzChasCompPowerSupply2=trpzChasCompPowerSupply2, trpzChasCompPowerSupply1=trpzChasCompPowerSupply1, trpzChasCompFan3=trpzChasCompFan3, PYSNMP_MODULE_ID=trpzRegistrationChassisMib, trpzChassisComponents=trpzChassisComponents, trpzRegistrationChassisMib=trpzRegistrationChassisMib, trpzChasCompFan1=trpzChasCompFan1, trpzChasCompPowerSupplies=trpzChasCompPowerSupplies, trpzChasCompFans=trpzChasCompFans)
