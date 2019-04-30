#
# PySNMP MIB module NTWS-REGISTRATION-CHASSIS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NTWS-REGISTRATION-CHASSIS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:16:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ntwsRegistration, = mibBuilder.importSymbols("NTWS-ROOT-MIB", "ntwsRegistration")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, IpAddress, ModuleIdentity, Counter32, NotificationType, MibIdentifier, TimeTicks, ObjectIdentity, Unsigned32, iso, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "IpAddress", "ModuleIdentity", "Counter32", "NotificationType", "MibIdentifier", "TimeTicks", "ObjectIdentity", "Unsigned32", "iso", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ntwsRegistrationChassisMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 5))
ntwsRegistrationChassisMib.setRevisions(('2007-08-22 00:00',))
if mibBuilder.loadTexts: ntwsRegistrationChassisMib.setLastUpdated('200708220000Z')
if mibBuilder.loadTexts: ntwsRegistrationChassisMib.setOrganization('Nortel Networks')
ntwsChassisComponents = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 4))
ntwsChasCompPowerSupplies = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 4, 1))
ntwsChasCompFans = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 4, 2))
ntwsChasCompPowerSupply1 = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 4, 1, 1))
ntwsChasCompPowerSupply2 = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 4, 1, 2))
ntwsChasCompFan1 = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 4, 2, 1))
ntwsChasCompFan2 = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 4, 2, 2))
ntwsChasCompFan3 = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 4, 2, 3))
mibBuilder.exportSymbols("NTWS-REGISTRATION-CHASSIS-MIB", ntwsChasCompPowerSupplies=ntwsChasCompPowerSupplies, ntwsRegistrationChassisMib=ntwsRegistrationChassisMib, ntwsChassisComponents=ntwsChassisComponents, ntwsChasCompFan3=ntwsChasCompFan3, ntwsChasCompFans=ntwsChasCompFans, PYSNMP_MODULE_ID=ntwsRegistrationChassisMib, ntwsChasCompPowerSupply1=ntwsChasCompPowerSupply1, ntwsChasCompFan1=ntwsChasCompFan1, ntwsChasCompPowerSupply2=ntwsChasCompPowerSupply2, ntwsChasCompFan2=ntwsChasCompFan2)
