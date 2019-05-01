#
# PySNMP MIB module FSS-COMMON-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FSS-COMMON-SMI
# Produced by pysmi-0.3.4 at Wed May  1 13:16:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, enterprises, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Bits, iso, Gauge32, ModuleIdentity, Integer32, Counter32, Unsigned32, MibIdentifier, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "enterprises", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Bits", "iso", "Gauge32", "ModuleIdentity", "Integer32", "Counter32", "Unsigned32", "MibIdentifier", "IpAddress", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
fujitsu = ModuleIdentity((1, 3, 6, 1, 4, 1, 211))
if mibBuilder.loadTexts: fujitsu.setLastUpdated('201605131500Z')
if mibBuilder.loadTexts: fujitsu.setOrganization('Fujitsu Network Communications, Inc.')
if mibBuilder.loadTexts: fujitsu.setContactInfo('Fujitsu Technical Assistance Center (FTAC), 1-800-USE-FTAC (1-800-873-3822)')
if mibBuilder.loadTexts: fujitsu.setDescription('This MIB module defines all of the base level headers used for control of the Fujitsu Network Communications, Inc. enterprises MIB tree. The main utility of this MIB module is to collect the MIB tree of the base objects in the fss branch.')
product = MibIdentifier((1, 3, 6, 1, 4, 1, 211, 1))
transport = MibIdentifier((1, 3, 6, 1, 4, 1, 211, 1, 24))
fssCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 211, 1, 24, 12))
mibBuilder.exportSymbols("FSS-COMMON-SMI", fujitsu=fujitsu, product=product, fssCommon=fssCommon, transport=transport, PYSNMP_MODULE_ID=fujitsu)
