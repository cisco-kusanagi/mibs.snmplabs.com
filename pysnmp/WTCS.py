#
# PySNMP MIB module WTCS (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WTCS
# Produced by pysmi-0.3.4 at Mon Apr 29 19:42:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
enterprises, Bits, Counter32, Counter64, Gauge32, Unsigned32, iso, ObjectIdentity, NotificationType, IpAddress, MibIdentifier, ModuleIdentity, Integer32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "Bits", "Counter32", "Counter64", "Gauge32", "Unsigned32", "iso", "ObjectIdentity", "NotificationType", "IpAddress", "MibIdentifier", "ModuleIdentity", "Integer32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
wtcs = ModuleIdentity((1, 3, 6, 1, 4, 1, 9600))
wtcs.setRevisions(('2004-02-29 06:16', '2003-11-26 00:00',))
if mibBuilder.loadTexts: wtcs.setLastUpdated('200402290616Z')
if mibBuilder.loadTexts: wtcs.setOrganization('Informant Systems, Inc.')
class InstanceName(TextualConvention, OctetString):
    status = 'current'
    displayHint = '64t'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

informant = MibIdentifier((1, 3, 6, 1, 4, 1, 9600, 1))
mibBuilder.exportSymbols("WTCS", InstanceName=InstanceName, PYSNMP_MODULE_ID=wtcs, informant=informant, wtcs=wtcs)
