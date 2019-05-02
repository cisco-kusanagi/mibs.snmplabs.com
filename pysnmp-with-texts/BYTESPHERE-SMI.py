#
# PySNMP MIB module BYTESPHERE-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BYTESPHERE-SMI
# Produced by pysmi-0.3.4 at Wed May  1 11:42:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Gauge32, Counter64, MibIdentifier, ObjectIdentity, Counter32, IpAddress, iso, TimeTicks, NotificationType, Integer32, ModuleIdentity, enterprises, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Gauge32", "Counter64", "MibIdentifier", "ObjectIdentity", "Counter32", "IpAddress", "iso", "TimeTicks", "NotificationType", "Integer32", "ModuleIdentity", "enterprises", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
bytesphere = ModuleIdentity((1, 3, 6, 1, 4, 1, 7013))
bytesphere.setRevisions(('2007-10-05 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: bytesphere.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: bytesphere.setLastUpdated('200710050000Z')
if mibBuilder.loadTexts: bytesphere.setOrganization('ByteSphere Technologies LLC')
if mibBuilder.loadTexts: bytesphere.setContactInfo(' ByteSphere Technologies LLC Postal: 955 Mass Ave #141 Cambridge, MA 02139 USA E-mail: bscustsupt@bytesphere.com')
if mibBuilder.loadTexts: bytesphere.setDescription('The MIB module to describe the SMI for BYTESPHERE applications.')
bytesphereMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 7013, 1))
mibBuilder.exportSymbols("BYTESPHERE-SMI", PYSNMP_MODULE_ID=bytesphere, bytesphere=bytesphere, bytesphereMgmt=bytesphereMgmt)
